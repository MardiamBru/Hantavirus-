# Guia Informativo Hantavírus

**[Acessar o site educativo](https://mardiambru.github.io/Hantavirus-/)**

Projeto acadêmico do curso de Sistemas Biomédicos da FATEC Bauru, 5º semestre, Microbiologia Aplicada (2026).

## Site

O arquivo `index.html` oferece sete abas: visão geral, transmissão, sintomas e cuidados, prevenção, imagens e materiais, folder em PDF e fontes. Funciona em celulares e computadores, permite navegação por teclado e impressão de todas as seções. Sem JavaScript, todas as seções ficam disponíveis na mesma página.

O GitHub Pages publica o conteúdo da branch `main`. Não há dependências de compilação. As imagens são carregadas de sites oficiais e têm créditos junto às figuras. Se uma imagem externa falhar, o acesso à fonte permanece disponível.

## Fontes consultadas em 01/09/2026

- [Ministério da Saúde — Hantavirose](https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/h/hantavirose)
- [CDC — About Hantavirus](https://www.cdc.gov/hantavirus/about/index.html)
- [CDC — How to Clean Up After Rodents](https://www.cdc.gov/healthy-pets/rodent-control/clean-up.html)
- [DIVE/SC — Hantavirose: o que é e o que fazer?](https://www.youtube.com/watch?v=U9Vbta8OXr4)

As fotografias CDC PHIL [1136](https://wwwn.cdc.gov/phil/Details.aspx?pid=1136) (Cynthia Goldsmith) e [8358](https://wwwn.cdc.gov/phil/Details.aspx?pid=8358) (James Gathany) são de domínio público. O roedor fotografado é uma espécie da América do Norte, identificado dessa forma na legenda. O infográfico de limpeza é reproduzido do CDC, com fonte indicada.

## Créditos

- Giovana Amancio
- Luiz Gustavo Brito Sinhoretti
- Milena Gasparotto
- Marcelo Dias Machado

## Folder da campanha

- `downloads/folder-hantavirus-A4.pdf`: PDF A4 com a composição do anexo, logotipo original, QR Code vetorial e orientação de limpeza revisada.
- `assets/qr-site.svg`: QR Code para `https://mardiambru.github.io/Hantavirus-/`, com margem de quatro módulos.
- `assets/folder-previa.jpg`: prévia do PDF exibida no site.
- `assets/folder-original.jpg`: referência original, utilizada para exibir o logotipo do curso por recorte visual no SVG do cabeçalho.
- `build_campaign.py`: fonte de construção do PDF e do QR Code; requer Python, Pillow e ReportLab.

O QR foi decodificado com sucesso diretamente da renderização final do PDF. A cópia JPG original permanece como referência, mas deve-se distribuir o PDF atualizado. O trecho sobre limpeza foi corrigido conforme o CDC. Impressão: papel A4 colorido, ajustar à área imprimível. A nitidez do conteúdo original é limitada à resolução da imagem fornecida.

## Materiais anteriores

Os arquivos `flyer.html`, `flyer.pdf`, `generate_flyer.py` e `INSTRUCOES_IMPRESSAO.md` foram preservados como versões anteriores. Não foram revisados nesta atualização; para compartilhar orientações atualizadas, utilize o site ou sua função de impressão.

## Uso educativo

Este projeto não substitui avaliação médica e não é uma publicação oficial dos órgãos citados. Direitos de materiais de terceiros permanecem com os respectivos titulares.
