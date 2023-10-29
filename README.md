# AIRacismFinder

# Projeto de Análise de Contextos Raciais com ChatGPT

Este projeto é uma implementação de um sistema de análise de contextos racistas utilizando a API da OpenAI. O objetivo é analisar conversas em busca de elementos racistas e fornecer um veredicto sobre a presença de racismo no contexto.

## Requisitos

- Python 3.x
- Biblioteca `openai` (instalável via `pip`)
- Biblioteca `tkinter` (instalável via `pip`)

## Configuração

Antes de executar o projeto, é necessário configurar a API da OpenAI e ter uma chave de API válida. Substitua o valor da variável `API_KEY` no arquivo `requirement.py` com a sua chave de API.

## Como Usar

1. Execute o script principal `racismo_detector.py`.
2. O programa solicitará que você forneça um arquivo de contexto. Certifique-se de que o arquivo contenha o contexto da conversa que você deseja analisar.
3. O Algoritmo de IA iniciará uma conversa usando o pretexto especificado no código e o conteúdo do arquivo de contexto.
4. O sistema analisará o contexto e fornecerá um veredicto sobre se a conversa é racista ou não, juntamente com um motivo, se aplicável.
5. Se o resultado for positivo, um pop-up de aviso será exibido com o motivo.
6. Se o resultado for negativo, a resposta do assistente será exibida no console.

Certifique-se de seguir as diretrizes do projeto para formatar o motivo do veredicto da maneira correta.

## Notas

- Este projeto é uma implementação básica e pode ser expandido para atender a requisitos adicionais ou integrado em sistemas mais complexos.
- Este projeto não substitui a avaliação humana e serve apenas como uma ferramenta de assistência na detecção de contextos racistas.
