# Python-BotNotepad-Test

Este projeto contém um bot simples em Python que utiliza a biblioteca **PyAutoGUI** para automatizar tarefas no computador. Especificamente, este bot abre o **Bloco de Notas** (Notepad) no Windows, escreve uma mensagem predefinida e simula a digitação no programa. O bot é útil para demonstração de automação de interface gráfica e interação com aplicativos desktop.

## Descrição

O script faz o seguinte:

1. Utiliza o PyAutoGUI para simular o pressionamento da tecla **Windows**.
2. Digita "notepad" para abrir o Bloco de Notas no Windows.
3. Pressiona **Enter** para abrir o programa.
4. Clica na janela do Bloco de Notas e digita a frase "Eu te Amo".
5. O código permite ainda descobrir a posição do cursor na tela com `pyautogui.position()`, útil para ajustar os cliques em locais específicos.

## Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação utilizada.
- **PyAutoGUI**: Biblioteca para automação de interface gráfica com o usuário (GUI).

## Como Rodar o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/Python-BotNotepad-Test.git

cd Python-BotNotepad-Test

pip install pyautogui

python BotSimples.py
```

## Personalizações
- Você pode modificar a frase que o bot escreve alterando a linha pyautogui.write("Eu te Amo").
- Para ajustar a posição do clique ou adicionar novas interações, utilize pyautogui.position() para encontrar as coordenadas corretas na tela.

