# Repositório de Boas Práticas Automatizadas 🚀

Este projeto visa automatizar a aplicação de boas práticas no terminal e Git, através da instalação de documentação local, hooks de shell, scripts de validação e wrappers para execução segura de comandos.

---

## Conteúdo do repositório

- `practices/` : Documentos em markdown com as melhores práticas para Git, Shell, Segurança, Automação, etc.  
- `hooks/pre_command_check.sh` : Script shell que intercepta comandos para emitir lembretes e alertas.  
- `wrapper.sh` : Script wrapper para executar comandos via validador Python.  
- `validate_command.py` : Script Python que valida comandos e retorna alertas.  
- `installer.py` : Script que instala documentações, hooks e wrappers automaticamente.

---

## Instalação

Para começar a usar, rode o instalador:

```bash
python3 installer.py
```

O script fará:

- Criação da pasta `practices/` com documentos de boas práticas.  
- Configuração do `~/.bashrc` para carregar o hook shell `pre_command_check.sh`.  
- Instalação do wrapper `run_validated_command.sh` em `~/bin` com alias configurado.

Após a instalação, abra um novo terminal para aplicar as configurações.

---

## Uso

- Para comandos comuns, o hook shell mostrará lembretes automáticos sobre boas práticas.  
- Para validação mais rigorosa, use o wrapper digitando:

```bash
run_validated_command <comando>
```

Por exemplo:

```bash
run_validated_command rm -rf /algum/caminho
```

O script validará e emitirá alertas, pedindo confirmação antes de executar o comando.

---

## Atualização automática das boas práticas

Após a instalação, um cron job será agendado automaticamente para executar todas as noites às 03:00 AM e atualizar as boas práticas das ferramentas detectadas.

Se desejar rodar a atualização manualmente, execute:

```bash
python3 /caminho/para/update_practices_cron.py
```

Para verificar se o cron job está ativo, use:

```bash
crontab -l
```

---

Se desejar remover o cron job, rode:

```bash
crontab -l | grep -v update_practices_cron.py | crontab -
```

---

## Atualização automática das boas práticas

Após a instalação, um cron job será agendado automaticamente para executar todas as noites às 03:00 AM e atualizar as boas práticas das ferramentas detectadas.

Se desejar rodar a atualização manualmente, execute:

```bash
python3 /caminho/para/update_practices_cron.py
```

Para verificar se o cron job está ativo, use:

```bash
crontab -l
```

Para remover o cron job, execute:

```bash
bash
crontab -l | grep -v update_practices_cron.py | crontab -
```

---

## Atualizações e contribuições

- O repositório pode ser atualizado para adicionar novas regras e práticas facilmente.  
- Contribuições são bem-vindas!  
- Para atualizar documentação e hooks, basta rodar o instalador novamente.