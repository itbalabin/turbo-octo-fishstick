import subprocess

subprocess.run(["pytest", "--alluredir=allure-results"])

subprocess.run(["allure", "generate", "allure-results", "-o", "allure-report"])

subprocess.run(["allure", "open", "allure-report"])