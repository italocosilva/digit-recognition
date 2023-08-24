import tkinter as tk
from PIL import Image, ImageDraw
from predict import predict


class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Digit Recognition")

        self.result = 0

        self.canvas = tk.Canvas(self.root, width=320, height=320, bg="black")
        self.canvas.pack()

        self.drawing = Image.new("RGB", (320, 320), "black")
        self.draw2 = ImageDraw.Draw(self.drawing)

        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

        # Botão para realizar a ação
        self.action_button = tk.Button(
            root, text="Predict", command=self.perform_action
        )
        self.action_button.pack()

        # Botão para limpar
        self.clear_button = tk.Button(root, text="Clear", command=self.clear)
        self.clear_button.pack()

        # Resultado da ação
        self.action_result = tk.StringVar()
        self.result_label = tk.Label(root, textvariable=self.action_result)
        self.result_label.pack()

        self.is_drawing = False
        self.prev_x = None
        self.prev_y = None

    def start_drawing(self, event):
        self.is_drawing = True
        self.prev_x = event.x
        self.prev_y = event.y

    def stop_drawing(self, event):
        self.is_drawing = False
        self.prev_x = None
        self.prev_y = None

    def draw(self, event):
        if (
            self.is_drawing
            and self.prev_x is not None
            and self.prev_y is not None
        ):
            x, y = event.x, event.y
            self.canvas.create_line(
                self.prev_x, self.prev_y, x, y, fill="white", width=20
            )
            self.draw2.line(
                [self.prev_x, self.prev_y, x, y], fill="white", width=20
            )
            self.prev_x = x
            self.prev_y = y

    def perform_action(self):
        pred = predict(self.drawing)
        self.action_result.set(f"Prediction: {pred}")

    def clear(self):
        self.canvas.delete("all")
        self.drawing = Image.new("RGB", (320, 320), "black")
        self.draw2 = ImageDraw.Draw(self.drawing)


# Configuração da janela
root = tk.Tk()
app = DrawingApp(root)

# Iniciar loop da interface
root.mainloop()
