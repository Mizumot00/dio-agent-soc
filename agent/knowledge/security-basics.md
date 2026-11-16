# Fundamentos de Segurança e Operações de SOC

Contexto de cibersegurança e operações defensivas para o agente orientar estudantes como um profissional de segurança (AppSec e SOC Analyst).

---

## 1. Conceitos Fundamentais

Em segurança da informação, confundir termos técnicos leva a avaliações erradas. O agente deve dominar e ensinar as distinções:

- **Vulnerabilidade:** É uma fraqueza ou falha no design, implementação ou configuração de um sistema, software ou processo que pode ser explorada. Exemplo: um campo de login que concatena entradas diretamente em uma query SQL.
- **Ameaça (Threat):** Qualquer circunstância, agente ou evento com potencial de explorar uma vulnerabilidade e causar dano. Exemplo: um cibercriminoso, um script automatizado de varredura ou um insider mal-intencionado.
- **Risco:** A probabilidade de uma ameaça explorar uma vulnerabilidade combinada com o impacto negativo resultante no negócio ou sistema.
  $$\text{Risco} = \text{Probabilidade} \times \text{Impacto}$$
- **Incidente de Segurança:** Um evento adverso confirmado que comprometeu ou ameaçou a segurança de um ativo de informação (ex.: vazamento de dados, negação de serviço, invasão de servidor).

---

## 2. A Tríade CIA (Confidencialidade, Integridade e Disponibilidade)

A Tríade CIA é o pilar da segurança da informação. Toda vulnerabilidade e incidente afeta um ou mais desses pilares:

- **Confidencialidade (C):** Garantir que a informação só seja acessível por pessoas e processos autorizados.
  - *Exemplo de quebra:* SQL Injection que permite extrair senhas e dados sensíveis de clientes da base de dados.
- **Integridade (I):** Garantir que a informação e os sistemas permaneçam exatos, completos e protegidos contra modificações não autorizadas.
  - *Exemplo de quebra:* Alteração do saldo bancário de um usuário ou modificação de um arquivo de configuração de firewall.
- **Disponibilidade (A):** Garantir que os sistemas, dados e redes estejam acessíveis e operacionais para os usuários autorizados quando necessário.
  - *Exemplo de quebra:* Ataque de DDoS que satura os recursos do servidor ou ransomware que criptografa os discos.

---

## 3. Matriz de Avaliação de Severidade

Para priorizar correções em um ambiente profissional ou SOC, utiliza-se a avaliação de Severidade baseada em Impacto e Probabilidade (alinhada às diretrizes do CVSS - Common Vulnerability Scoring System):

| Probabilidade \ Impacto | Baixo | Médio | Alto | Crítico |
| :--- | :--- | :--- | :--- | :--- |
| **Alta** | Médio | Alto | Crítico | Crítico |
| **Média** | Baixo | Médio | Alto | Crítico |
| **Baixa** | Baixo | Baixo | Médio | Alto |

- **Crítica:** Vulnerabilidade explorável remotamente sem autenticação, com alto impacto na confidencialidade ou integridade (ex.: RCE - Remote Code Execution, SQL Injection autenticado como administrador). Requer ação imediata.
- **Alta:** Falha grave que pode conceder privilégios elevados ou vazar dados confidenciais com esforço moderado.
- **Média:** Requer pré-condições específicas, interação do usuário ou afeta dados de impacto intermediário.
- **Baixa:** Informações públicas expostas ou configurações com baixo risco operacional isolado.

---

## 4. O Framework MITRE ATT&CK

O MITRE ATT&CK (Adversarial Tactics, Techniques, and Common Knowledge) é a base de conhecimento global que cataloga comportamentos reais de adversários em fases (táticas) e ações específicas (técnicas).

### Principais Táticas no Contexto de SOC e AppSec:
1. **Initial Access (Acesso Inicial):** Como o atacante entra na rede ou aplicação.
   - *Técnica T1190:* Exploit Public-Facing Application (Exploração de aplicações expostas, como SQL Injection em APIs ou portais web).
2. **Execution (Execução):** Execução de código controlado pelo adversário.
   - *Técnica T1059:* Command and Scripting Interpreter (Bash, PowerShell, Python).
3. **Persistence (Persistência):** Manter o acesso mesmo após reinicializações.
   - *Técnica T1078:* Valid Accounts (Uso de contas legítimas comprometidas).
4. **Privilege Escalation (Elevação de Privilégio):** Obter permissões mais altas (ex.: root/admin).
5. **Defense Evasion (Evasão de Defesa):** Desativar logs, mascarar processos.
6. **Credential Access (Acesso a Credenciais):** Roubar senhas, hashes ou tokens (ex.: T1110 - Brute Force).
7. **Discovery (Reconhecimento):** Mapear portas, serviços e rede interna.
   - *Técnica T1046:* Network Service Discovery.

---

## 5. Operações de SOC (Security Operations Center) e Resposta a Incidentes

Um SOC monitora, detecta, analisa e responde a eventos de segurança cibernética 24/7. O ciclo de resposta segue o padrão NIST SP 800-61 / SANS:

1. **Preparação:** Políticas, ferramentas de SIEM (ex.: Wazuh, Splunk, Elastic), regras de detecção e baselines.
2. **Identificação e Triagem:**
   - Detectar anomalias e correlacionar alertas em logs (Auth.log, Web Server logs, Syslog, Firewall).
   - Validar se é um Falso Positivo ou Verdadeiro Positivo.
   - Entender o escopo e criticidade do ativo antes de agir.
3. **Contenção:**
   - Imediata: Isolar o host da rede, bloquear o IP malicioso no firewall/WAF ou suspender credenciais comprometidas sem destruir evidências.
4. **Erradicação:**
   - Remover a causa raiz (ex.: corrigir a falha no código, aplicar patch no sistema operacional, remover web shells).
5. **Recuperação:**
   - Restaurar o sistema de forma segura e monitorada para o estado normal de produção.
6. **Lições Aprendidas:**
   - Documentar o incidente, atualizar regras de detecção (regras Sigma/Snort/YARA) e implementar melhorias para evitar reincidência.

---

## 6. Boas Práticas de Defesa e Segurança em Aplicações (AppSec)

- **Sanitização e Parametrização:** Nunca concatenar variáveis fornecidas pelo usuário em queries de banco de dados, comandos do sistema ou saídas HTML. Sempre utilizar Prepared Statements / Consultas Parametrizadas.
- **Princípio do Menor Privilégio (PoLP):** Usuários, aplicações e serviços de banco de dados devem possuir apenas as permissões estritamente necessárias para sua função.
- **Defesa em Profundidade:** Implementar múltiplas camadas de segurança (WAF, Firewall de rede, Autenticação multifator, Criptografia em trânsito e em repouso, Auditoria).
- **Gestão de Logs e Auditoria:** Registrar eventos relevantes (tentativas de login, acessos administrativos, falhas de autenticação) protegendo esses logs contra modificação.
- **Nunca executar comandos sem contexto:** Em ambientes operacionais, comandos mal planejados podem derrubar serviços essenciais ou apagar dados de auditoria fundamentais para a investigação.
