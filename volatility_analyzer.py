import argparse
import os
import subprocess
import re
import platform
from typing import List, Dict, Any
from jinja2 import Template
from datetime import datetime
import inspect

class PluginAnalyzer:
    def analyze(self, output: str) -> List[Dict[str, Any]]:
        raise NotImplementedError("Cette méthode doit être implémentée par les sous-classes")

class DefaultAnalyzer(PluginAnalyzer):
    def analyze(self, output: str) -> List[Dict[str, Any]]:
        return [{"raw_output": line} for line in output.split('\n') if line.strip()]

class PslistAnalyzer(PluginAnalyzer):
    def analyze(self, output: str) -> List[Dict[str, Any]]:
        results = []
        for line in output.split('\n')[2:]:
            parts = line.split()
            if len(parts) >= 4:
                results.append({
                    "type": "process",
                    "name": parts[1],
                    "pid": parts[2],
                    "ppid": parts[3]
                })
        return results

class NetscanAnalyzer(PluginAnalyzer):
    def analyze(self, output: str) -> List[Dict[str, Any]]:
        results = []
        for line in output.split('\n')[2:]:
            parts = line.split()
            if len(parts) >= 5:
                results.append({
                    "type": "network",
                    "protocol": parts[0],
                    "local_address": parts[2],
                    "foreign_address": parts[3],
                    "state": parts[4]
                })
        return results

class FilescanAnalyzer(PluginAnalyzer):
    def analyze(self, output: str) -> List[Dict[str, Any]]:
        results = []
        file_pattern = r'(\S+)\s+(\S+)\s+(\S+)\s+(.*?\.[\w]+)'
        matches = re.findall(file_pattern, output, re.IGNORECASE)
        for match in matches:
            results.append({
                "type": "file",
                "offset": match[0],
                "file_type": match[2],
                "file_name": match[3]
            })
        return results

class MalfindAnalyzer(PluginAnalyzer):
    def analyze(self, output: str) -> List[Dict[str, Any]]:
        results = []
        sections = output.split('\n\n')
        for section in sections:
            if 'Process:' in section and 'VadTag:' in section:
                process = re.search(r'Process:\s+(\S+)', section)
                vadtag = re.search(r'VadTag:\s+(\S+)', section)
                if process and vadtag:
                    results.append({
                        "type": "malware",
                        "process": process.group(1),
                        "vadtag": vadtag.group(1)
                    })
        return results

class EnvarsAnalyzer(PluginAnalyzer):
    def analyze(self, output: str) -> List[Dict[str, Any]]:
        results = []
        for line in output.split('\n')[2:]:
            parts = line.split()
            if len(parts) >= 4:
                results.append({
                    "type": "envvar",
                    "process": parts[1],
                    "pid": parts[2],
                    "variable": parts[3],
                    "value": ' '.join(parts[4:])
                })
        return results
    
class HandleAnalyzer(PluginAnalyzer):
    def analyze(self, output: str) -> List[Dict[str, Any]]:
        results = []
        for line in output.split('\n')[2:]:
            parts = line.split()
            if len(parts) >= 7:
                results.append({
                    "type": "handle",
                    "pid": parts[0],
                    "process": parts[1],
                    "offset": parts[2],
                    "handlevalue": parts[3],
                    "handletype": parts[4],
                    "grantedaccess": parts[5],
                    "name": ' '.join(parts[6:])
                })
        return results

class CmdlineAnalyzer(PluginAnalyzer):
    def analyze(self, output: str) -> List[Dict[str, Any]]:
        results = []
        for line in output.split('\n')[2:]:
            parts = line.split(maxsplit=2)
            if len(parts) >= 3:
                results.append({
                    "type": "cmdline",
                    "pid": parts[0],
                    "process": parts[1],
                    "cmdline": parts[2]
                })
        return results

class DlllistAnalyzer(PluginAnalyzer):
    def analyze(self, output: str) -> List[Dict[str, Any]]:
        results = []
        current_process = None
        for line in output.split('\n')[2:]:
            if line.startswith('*'): 
                parts = line.split()
                current_process = {
                    "pid": parts[3],
                    "process": parts[1],
                    "dlls": []
                }
                results.append(current_process)
            elif current_process and line.strip():
                parts = line.split()
                if len(parts) >= 4:
                    current_process["dlls"].append({
                        "base": parts[0],
                        "size": parts[1],
                        "name": parts[2],
                        "path": ' '.join(parts[3:])
                    })
        return results

def get_analyzer(plugin_name: str) -> PluginAnalyzer:
    analyzer_name = f"{plugin_name.capitalize()}Analyzer"
    analyzer_class = globals().get(analyzer_name, DefaultAnalyzer)
    return analyzer_class()

def detect_host_os() -> str:
    system = platform.system().lower()
    if system in ["linux", "darwin", "windows"]:
        return system
    else:
        raise ValueError(f"Système d'exploitation non pris en charge : {system}")

def detect_image_os_type(image_file: str) -> str:
    for os_type in ['windows', 'linux', 'mac']:
        command = f"vol -f {image_file} {os_type}.info"
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
            if any(key in result.stdout for key in ['Kernel Base', 'Linux version', 'Darwin Kernel Version']):
                return os_type
        except subprocess.CalledProcessError:
            pass
    raise ValueError("Impossible de déterminer le type de système d'exploitation de l'image mémoire.")

def get_available_plugins() -> List[str]:
    plugins = []
    for name, obj in globals().items():
        if inspect.isclass(obj) and issubclass(obj, PluginAnalyzer) and obj != PluginAnalyzer and obj != DefaultAnalyzer:
            plugins.append(name.lower().replace('analyzer', ''))
    return plugins

def select_plugins(available_plugins: List[str]) -> List[str]:
    print("Plugins disponibles:")
    for i, plugin in enumerate(available_plugins, 1):
        print(f"{i}. {plugin}")
    print("\nEntrez les numéros ou les noms des plugins que vous souhaitez exécuter, séparés par des espaces.")
    print("Exemple: 1 3 envars")

    while True:
        selection = input("Votre sélection: ").split()
        selected_plugins = []
        for item in selection:
            if item.isdigit() and 1 <= int(item) <= len(available_plugins):
                selected_plugins.append(available_plugins[int(item) - 1])
            elif item.lower() in available_plugins:
                selected_plugins.append(item.lower())
        
        if selected_plugins:
            return selected_plugins
        else:
            print("Sélection invalide. Veuillez réessayer.")

def run_volatility_plugin(image_file: str, plugin: str, image_os: str) -> str:
    command = f"vol -f {image_file} {image_os}.{plugin}"
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution du plugin '{plugin}': {e.stderr}")
        return ""

def generate_html_report(analysis_results: Dict[str, Any], output_file: str) -> None:
    template = Template("""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Rapport d'analyse d'image mémoire</title>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; }
            h1, h2 { color: #2c3e50; }
            table { border-collapse: collapse; width: 100%; margin-bottom: 20px; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
        </style>
    </head>
    <body>
        <h1>Rapport d'analyse d'image mémoire</h1>
        <p>Date de l'analyse : {{ analysis_results.timestamp }}</p>
        <p>Système d'exploitation de l'hôte : {{ analysis_results.host_os }}</p>
        <p>Système d'exploitation de l'image : {{ analysis_results.image_os }}</p>
        <p>Plugins utilisés : {{ ', '.join(analysis_results.plugins) }}</p>
        
        {% for plugin, data in analysis_results.plugin_results.items() %}
        <h2>Résultats du plugin {{ plugin }}</h2>
        {% if data %}
        <table>
            <tr>
                {% for key in data[0].keys() %}
                <th>{{ key }}</th>
                {% endfor %}
            </tr>
            {% for item in data %}
            <tr>
                {% for value in item.values() %}
                <td>{{ value }}</td>
                {% endfor %}
            </tr>
            {% endfor %}
        </table>
        {% else %}
        <p>Aucun résultat pour ce plugin.</p>
        {% endif %}
        {% endfor %}
    </body>
    </html>
    """)
    
    html_content = template.render(analysis_results=analysis_results)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

def main():
    parser = argparse.ArgumentParser(description="Analyse d'image mémoire avec Volatility")
    parser.add_argument("image_file", help="Chemin vers le fichier d'image mémoire à analyser")
    parser.add_argument("--output", default="rapport_analyse.html", help="Nom du fichier de rapport HTML")
    args = parser.parse_args()

    if not os.path.exists(args.image_file):
        print(f"Erreur : Le fichier {args.image_file} n'existe pas.")
        return

    try:
        host_os = detect_host_os()
        print(f"Système d'exploitation de l'hôte détecté : {host_os}")

        image_os = detect_image_os_type(args.image_file)
        print(f"Système d'exploitation de l'image détecté : {image_os}")

        available_plugins = get_available_plugins()
        selected_plugins = select_plugins(available_plugins)
        print(f"Plugins sélectionnés : {', '.join(selected_plugins)}")

        analysis_results = {
            "timestamp": datetime.now().isoformat(),
            "host_os": host_os,
            "image_os": image_os,
            "plugins": selected_plugins,
            "plugin_results": {}
        }

        for plugin in selected_plugins:
            plugin_output = run_volatility_plugin(args.image_file, plugin, image_os)
            if plugin_output:
                analyzer = get_analyzer(plugin)
                analysis_results["plugin_results"][plugin] = analyzer.analyze(plugin_output)
            else:
                print(f"Aucune sortie pour le plugin {plugin}")

        generate_html_report(analysis_results, args.output)
        print(f"Rapport d'analyse généré : {args.output}")

    except Exception as e:
        print(f"Une erreur est survenue : {str(e)}")

if __name__ == "__main__":
    main()