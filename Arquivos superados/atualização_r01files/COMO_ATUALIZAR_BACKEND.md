# Como atualizar o backend (auditoria de planta com nota)

A análise de planta agora é uma **auditoria**: a IA recebe a planta de combate a incêndio
(e o memorial, se enviado) e responde se está conforme as ITs, com **nota de 0 a 10 + status**
(ex.: "8,5 — Apto com ressalvas"), listando cada sistema como **conforme / não conforme / pendente**.

Para isso funcionar, é preciso substituir **3 arquivos** no seu repositório do GitHub
(o mesmo que o Railway publica). São estes, na pasta `backend/`:

| Arquivo que eu gerei            | Onde colar no seu repositório      |
|---------------------------------|------------------------------------|
| `prompts.py`                    | `backend/ai/prompts.py`            |
| `plant_analysis.py`             | `backend/ai/plant_analysis.py`     |
| `main.py`                       | `backend/main.py`                  |

## Jeito mais simples (pelo site do GitHub, sem instalar nada)

Faça para cada um dos 3 arquivos:

1. Entre no seu repositório no GitHub (`renaldyoliveira4-dotcom/ppci-saas_01`).
2. Navegue até o arquivo (ex.: pasta `backend` → `ai` → `prompts.py`).
3. Clique no ícone de **lápis** (Edit this file), no canto superior direito do arquivo.
4. **Apague todo o conteúdo** e **cole** o conteúdo do arquivo novo que eu gerei (abra o meu arquivo, copie tudo).
5. Clique em **Commit changes** (botão verde).
6. Repita para os outros dois arquivos.

> Dica: comece por `prompts.py` e `plant_analysis.py` (pasta `backend/ai/`), depois `main.py` (pasta `backend/`).

## O que acontece depois

- Como o Railway tem **deploy automático** ligado (você viu "Auto deploys when pushed to GitHub"),
  assim que você der o último commit ele **republica sozinho** em 1–2 minutos.
- Não precisa mexer em mais nada: a chave da IA continua igual, a URL continua a mesma.

## Como testar se deu certo

1. Espere o Railway terminar (status volta para **Online**).
2. No app (`ppcipro.tiiny.site`), faça **Ctrl + F5** e vá em **Análise de Planta**.
3. Envie uma planta (PDF) e, se quiser, anexe o memorial.
4. Clique em **Auditar com IA**. Agora deve aparecer:
   - A **nota (0–10)** num círculo colorido + o **status** ("Apto a protocolar", etc.);
   - A lista **Sistemas exigidos × encontrados** com ✓ (conforme), ⚠ (pendente) ou ✗ (não conforme);
   - Divergências entre planta e memorial (se houver).

## Importante (limites honestos)

- A IA lê **PDF e imagens** (PNG/JPG). Arquivos **CAD (DWG/DXF/RVT/IFC)** não são lidos direto —
  o sistema pede para exportar em PDF. Isso já estava assim e continua.
- A auditoria é **orientativa**: ajuda muito na triagem, mas não substitui a análise do
  profissional habilitado nem a aprovação oficial do CBMBA. O app já mostra esse aviso.
- O custo por análise sobe um pouco quando você envia **planta + memorial** (dois documentos),
  porque a IA lê mais páginas. Continua na casa de centavos de dólar por análise.
