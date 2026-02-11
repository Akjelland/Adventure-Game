import tkinter as tk


root = tk.Tk()
root.title("Adventure Game")
root.geometry("400x300")


story = {
    "start": {
        "question": "You are in a forest. Which way do you go?",
        "choices": {"a": "Go left", "b": "Go right"},
        "next": {"a": "river", "b": "cave"}
    },
    "river": {
        "question": "You find a river. What do you do?",
        "choices": {"a": "Swim across", "b": "Build a raft"},
        "next": {"a": "swim_fail", "b": "raft_success"}
    },
    "cave": {
        "question": "You enter a dark cave. What do you do?",
        "choices": {"a": "Light a torch", "b": "Go back"},
        "next": {"a": "torch_success", "b": "start"}
    },
    "swim_fail": {
        "question": "You tried to swim but got swept away. Game over!",
        "choices": {},
        "next": {}
    },
    "raft_success": {
        "question": "You built a raft and crossed safely. You win!",
        "choices": {},
        "next": {}
    },
    "torch_success": {
        "question": "The torch lights up the cave. You find treasure. You win!",
        "choices": {},
        "next": {}
    }
}


question_label = tk.Label(root, text="", wraplength=380)
question_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

end_label = tk.Label(root, text="")
end_label.pack(pady=10)


def ask_question(node_key):
    node = story[node_key]


    question_label.config(text=node["question"])


    for widget in button_frame.winfo_children():
        widget.destroy()


    if not node["choices"]:
        end_label.config(text="The adventure ends here.")
        return

    for key, choice_text in node["choices"].items():
        btn = tk.Button(
            button_frame,
            text=f"{key}. {choice_text}",
            width=25,
            command=lambda k=key: ask_question(node["next"][k])
        )
        btn.pack(pady=2)
ask_question("start")
quitbutton=tk.Button(root,text="Quit",command=root.destroy)
quitbutton.pack()
retrybutton=tk.Button(root,text="Again?",command=lambda : ask_question("start"))
retrybutton.pack()
root.mainloop()




