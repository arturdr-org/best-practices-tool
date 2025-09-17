# 🚀 Repositório de Boas Práticas Automatizadas

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org/)
<!-- Add GitHub Actions Workflow Status Badge here if applicable -->
<!-- Example: ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/arturdrr/best-practices-tool/main?label=build) -->

Este projeto tem como objetivo automatizar a aplicação de boas práticas no terminal e Git, fornecendo documentação, validações e lembretes no ambiente do usuário para maior segurança e eficiência.

---

## 📚 Conteúdo do Repositório

- `practices/` : Documentos em markdown com as melhores práticas para Git, Bash, Segurança, Automação etc.  
- `hooks/pre_command_check.sh` : Script shell que intercepta comandos e mostra alertas antes da execução.  
- `wrapper.sh` : Wrapper para executar comandos via validador Python com confirmação interativa.  
- `validate_command.py` : Script em Python que valida comandos e emite alertas ou bloqueios.  
- `installer.py` : Instalador automático que configura todo ambiente, incluindo cron jobs para atualização.  
- `update_practices_cron.py` : Script para atualização automática diária das boas práticas conforme ferramentas detectadas.  
- `config.yaml` : Arquivo de configuração para ativar/desativar globalmente ou por ferramenta o sistema de boas práticas.

---

## ⚙️ Instalação

Execute o instalador com:

```bash
python3 installer.py
```

Ele fará:

- Criação da pasta `practices/` com os documentos locais.  
- Configuração automática do hook shell para alertas no terminal.  
- Instalação do wrapper shell com alias `run_validated_command`.  
- Criação do arquivo `config.yaml` padrão.  
- Agendamento de cron job para atualizar automaticamente boas práticas.

Reabra o terminal para aplicar as alterações.

---

## 🖥️ Uso

### Hook Shell (alertas automáticos)

O hook shell é ativado no terminal automaticamente e mostra alertas e dicas enquanto você digita comandos, como:

- ⚠️ Aviso ao usar `rm` sem `-i` para evitar exclusões acidentais  
- 💡 Sugestão para usar `git pull` antes de `git push`  
- ⚠️ Alerta para uso cuidadoso do `sudo`

### Wrapper Shell (validação ativa)

Para rodar comandos validados com confirmação, use o alias:

```bash
run_validated_command <comando>
```

Exemplo:

```bash
run_validated_command rm -rf /diretorio/importante
```

Se o comando tiver riscos, o validador emite alertas e pede confirmação antes de executar.

---

## 🔄 Atualização automática

Uma tarefa agendada via cron roda diariamente às 3h da manhã atualizando as boas práticas específicas para ferramentas detectadas (Docker, Terraform, Ansible, etc.).

Para rodar manualmente:

```bash
python3 update_practices_cron.py
```

Para verificar o cron job:

```bash
crontab -l
```

Para removê-lo:

```bash
crontab -l | grep -v update_practices_cron.py | crontab -
```

---

## 🔧 Configuração

Edite o arquivo `config.yaml` para ativar ou desativar:

- O sistema todo (`enabled: true/false`)  
- Boas práticas para ferramentas específicas, adicionando nomes em `disabled_tools`

Exemplo:

```yaml
enabled: true
disabled_tools:
  - docker
  - terraform
```

---

## 📖 Conteúdos externos

O projeto também baixa automaticamente conteúdos relevantes de repositórios externos com melhores práticas, armazenando localmente em:

```
external/practice-git/
external/git-practice/
```

Assim seu ambiente sempre estará atualizado com as melhores referências.

---

## 🤝 Contribuições e melhorias

Aceitamos sugestões e PRs para:

- Expandir as regras de validação  
- Melhorar os scripts de instalação e atualização  
- Integrar com mais ferramentas e IDEs  
- Otimizar a experiência do usuário no terminal

---

### 🚀 Comece agora!

Clone o repositório, rode o instalador e desfrute de um terminal mais seguro, produtivo e alinhado às melhores práticas!

---

Se precisar de ajuda para configurar ou personalizar, conte comigo! 😄