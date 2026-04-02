# 🛡️ SentinelPass - Web Password Analyzer

O **SentinelPass** é uma aplicação web focada em Segurança da Informação. Ele analisa a força de senhas criadas pelo usuário em tempo real, utilizando um motor de busca de padrões (Regex) no Backend para classificar a vulnerabilidade dos dados.

## 🚀 Diferencial do Projeto
Diferente de scripts básicos, este projeto utiliza o framework **Flask** para criar uma ponte entre o Python e uma interface Web (HTML/CSS). Ele demonstra o fluxo completo de uma aplicação:
1. **Entrada:** O usuário envia nome e senha pelo navegador.
2. **Processamento:** O Backend em Python valida os requisitos de segurança.
3. **Persistência:** O sistema gera um log de auditoria em `JSON` com data e nota da análise.
4. **Saída:** O resultado é devolvido dinamicamente para a tela do usuário.

## 🛠️ Tecnologias Utilizadas
* **Python 3**: Lógica principal e processamento.
* **Flask**: Framework web para gerenciamento de rotas e templates.
* **Jinja2**: Motor de renderização para exibir dados dinâmicos no HTML.
* **JSON & Regex**: Armazenamento de logs e filtragem de padrões de segurança.
* **HTML5 & CSS3**: Interface do usuário simples e responsiva.

## 📂 Estrutura do Repositório
* `sentinel.py`: O servidor Flask e lógica de segurança.
* `templates/index.html`: A interface visual do sistema.
* `logs_seguranca.json`: Histórico das análises realizadas (gerado automaticamente).
