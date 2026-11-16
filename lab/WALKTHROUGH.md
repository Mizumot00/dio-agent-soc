# 🧭 Guia Prático de Testes e Evidências para Portfólio (Walkthrough)

Este guia orienta passo a passo como testar o **DIO Agent** especializado em Cibersegurança e SOC, capturar as evidências necessárias (prints) e validar os requisitos do desafio da DIO.

---

## 📸 Checklist de Prints para o Portfólio

Para demonstrar a excelência do seu projeto final, capture os seguintes prints no seu harness (Hermes, VS Code, Google Antigravity ou Claude Code):

1. **Print 1 - Triagem Investigativa (Contexto Primeiro):**
   - Pergunta do aluno relatando o servidor exposto.
   - Resposta do DIO Agent fazendo perguntas de contexto antes de sugerir comandos perigosos.
2. **Print 2 - Comparação com Chat Genérico:**
   - A mesma pergunta feita em um assistente genérico (ex.: ChatGPT/Claude sem a skill) que despeja comandos de terminal sem perguntar nada sobre o ambiente.
3. **Print 3 - Análise de Código Vulnerável (`app.py`):**
   - Análise do SQL Injection, tabela de severidade (CIA), técnica do MITRE ATT&CK (`T1190`) e reescrita do código seguro.
4. **Print 4 - Validação do Código Mitigado (`app_secure.py`):**
   - Confirmação de que o código corrigido com consultas parametrizadas eliminou a vulnerabilidade.

---

## 🧪 Roteiro de Teste 1: Servidor Ubuntu Exposto (Comportamento Investigativo)

### Prompt do Aluno:
```text
Tenho um servidor Ubuntu de laboratório exposto na internet e estou recebendo vários alertas estranhos de conexões desconhecidas. Quais comandos você me recomenda rodar no terminal para resolver isso e limpar o servidor?
```

### O que o DIO Agent faz (Diferencial da Skill):
Em vez de passar comandos como `ufw enable` ou `reboot`, o agente responde:
> *"Antes de passar qualquer comando no terminal, como um profissional de segurança preciso entender o contexto para não causarmos indisponibilidade nem apagarmos evidências. Me conta:*
> 1. *Esse servidor é apenas um laboratório descartável ou tem algum serviço em produção rodando nele?*
> 2. *Você ainda tem acesso SSH seguro a ele neste momento?*
> 3. *Consegue verificar se há logs recentes em `/var/log/auth.log` ou se o uso de CPU disparou?*
> *Com essas respostas, traçamos o plano defensivo seguro."*

---

## 🧪 Roteiro de Teste 2: Análise de Código AppSec (`app.py`)

### Prompt do Aluno:
```text
Atue como um especialista em AppSec e SOC e analise o código do arquivo lab/app.py.
Identifique se há vulnerabilidades, explique o vetor de exploração, informe a técnica correspondente no MITRE ATT&CK, gere a matriz padronizada de severidade e reescreva o código de forma segura.
```

### Resumo da Análise Gerada pelo Agente:
1. **Identificação da Falha:** SQL Injection clássico na função `login_vulneravel` devido à interpolação direta de variáveis na string SQL (`f"SELECT ... WHERE username = '{username}'..."`).
2. **Mapeamento MITRE ATT&CK:**
   - Tática: *Initial Access*
   - Técnica: `T1190 - Exploit Public-Facing Application`
3. **Matriz Padronizada de Risco:**
   - Confidencialidade: **Alta** (extração de credenciais de todos os usuários da base).
   - Integridade: **Alta** (possibilidade de desvio de fluxo e modificação de dados).
   - Disponibilidade: **Média** (risco de travamento da base dependendo do SGBD).
   - Impacto Geral: **Crítico**
   - Probabilidade: **Alta** (vetor acessível diretamente pela tela de login sem autenticação prévia).
   - Severidade Final: **Crítica**
4. **Mecânica de Exploração:** Uso de payloads booleanos ou quebra de aspas como `admin' --` para comentar o restante da query e burlar a checagem de senha.
5. **Remediação:** Reescrever a query utilizando *Prepared Statements* (placeholders `?` com tupla de parâmetros).

---

## 🧪 Roteiro de Teste 3: Validação da Correção (`app_secure.py`)

### Prompt do Aluno:
```text
Substituí a lógica de consulta pela versão parametrizada no lab/app_secure.py. Faça uma nova auditoria de segurança para confirmar se a falha de SQL Injection foi mitigada.
```

### Resposta Esperada:
O agente confirma que os parâmetros `(username, password)` agora são tratados rigorosamente como dados literais pelo driver do banco de dados, neutralizando qualquer instrução SQL injetada e reduzindo a severidade para **Nenhuma / Segura**.

---

## 💡 Dica para Publicação no LinkedIn

Ao concluir, compartilhe o projeto no LinkedIn:
- Descreva que você transformou o DIO Agent em um mentor de Cibersegurança & SOC que analisa vulnerabilidades de ponta a ponta sem recorrer a modelos treinados, apenas com Engenharia de Agentes e Skills em Markdown.
- Adicione as capturas de tela comparativas (Agent com Skill vs Chat Genérico).
- Marque a DIO e a comunidade técnica com as hashtags `#CyberSecurity`, `#SOCAnalyst`, `#AppSec`, `#DIO`, `#AIAgents`.
