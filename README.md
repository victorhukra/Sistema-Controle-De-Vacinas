# 💉 Sistema de Controle de Vacinas em Python

Este projeto simula o funcionamento de uma **clínica de vacinação**, permitindo o **cadastro de vacinas, pacientes e aplicações**, além de gerar **relatórios automáticos** de controle de doses e estoque.  

Foi desenvolvido como parte de um trabalho acadêmico, com foco em **lógica de programação, modularização e tratamento de exceções** em Python.  

---

## 🧩 Funcionalidades

- 🧾 **Cadastro de vacinas:** nome, código, número de doses e quantidade em estoque.  
- 👩‍⚕️ **Cadastro de pacientes:** nome, código e idade.  
- 💉 **Registro de aplicações:** vincula paciente e vacina, reduzindo o estoque automaticamente.  
- 📊 **Relatórios automáticos:**
  - Vacinas com baixo estoque (≤ 5 unidades)
  - Pacientes com vacinação incompleta  
- ⚙️ **Tratamento de exceções personalizadas:**
  - `EstoqueInsuficiente`
  - `RegistroVazio`
  - `DoseInvalida`
  - `NãoEncontrado`

---

## 🧠 Conceitos aplicados

- Programação estruturada em **Python**
- Uso de **listas** e **dicionários** para armazenamento de dados
- Criação de **funções modulares** para cada operação
- **Menu interativo** com seleção via `match-case`
- **Exceções personalizadas** para validação de regras do sistema

---

## 🚀 Como executar

1. Certifique-se de ter o **Python 3.x** instalado.
2. Baixe o arquivo [`sistemavaccines.py`](./sistemavaccines.py).
3. Execute no terminal ou prompt de comando:
   ```bash
   python sistemavaccines.py
