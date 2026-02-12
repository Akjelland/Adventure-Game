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
        "question": "You built a raft and crossed safely. what now?",
        "choices": {"a":"talk to stranger","b":"go to mountain"},
        "next": {"a":"stranger","b":"mountain"}
    },
        "stranger": {
        "question": "You walk up to the stranger, What will you do?",
        "choices": {"a":"awkwardly leave","b":"ask for information"},
        "next": {"a":"raft_success","b":"information"}
    },
        "information": {
        "question": "the stranger tells you about a dragon in a castle near here. What now?",
        "choices": {"a":"thank stranger","b":"leave"},
        "next": {"a":"thank_stranger","b":"leave_mean"}
    },
        "thank_stranger": {
        "question": "You thank the stranger and then peacefully leave. what now?",
        "choices": {"a":"go to mountain","b":"go to village"},
        "next": {"a":"mountain","b":"village"}
    },
        "village": {
        "question": "You go to the village and live a peaceful life. You win!",
        "choices": {},
        "next": {}
    },
        "leave_mean": {
        "question": "The stranger is not pleased by your lack of manners and kills you. You lose!",
        "choices": {},
        "next": {}
    },
        "mountain": {
        "question": "you go towards the mountain and come accross a castle surounded by lava. what now?",
        "choices": {"a":"turn around","b":"enter castle"},
        "next": {"a":"raft_success","b":"castle"}
    },
        "castle": {
        "question": "You enter the castle it seems very warn down. what now?",
        "choices": {"a":"grand room adorned in gold","b":"dark hallway"},
        "next": {"a":"grand_room","b":"dark_hallway"}
    },
        "dark_hallway": {
        "question": "You enter the hallway and see a couple rooms. What now?",
        "choices": {"a":"Room 1","b":"Room 2"},
        "next": {"a":"room_1","b":"room_2"}
    },
        "room_1": {
        "question": "You find the treasury! You make your great escape and live a life of luxury. You win!",
        "choices": {},
        "next": {}
    },
        "room_2": {
        "question": "You enter the room and notice a large hole in the wall that appears to go to a large room. What now?",
        "choices": {"a":"approach hole","b":"leave room"},
        "next": {"a":"ledge_scene","b":"dark_hallway"}
    },
        "ledge_scene": {
        "question": "You see a dragon and a large chandelier attached by a chain. What now?",
        "choices": {"a":"attempt to break chain","b":"leave room"},
        "next": {"a":"chain_scene","b":"dark_hallway"}
    },
        "chain_scene": {
        "question": "You sucessfully break the chain and it falls and hits the dragon killing it! You win!",
        "choices": {},
        "next": {}
    },
        "grand_room": {
        "question": "Its a dragon! What now?",
        "choices": {"a":"turn back","b":"bravely fight"},
        "next": {"a":"castle","b":"bravely_fight"}
    },
        "bravely_fight": {
        "question": "You go to confront the dragon but notice you are extremely underprepared and you die bravely fighting. You lose but bravely!",
        "choices": {},
        "next": {}
    },
    "torch_success": {
        "question": "You see the cave branches in two directions. What do you do?",
        "choices": {"a":"right path","b":"left path"},
        "next": {"a":"right_path","b":"left_path"}
    },
    "right_path": {
        "question": "you go right and see 2 chests, Which will you choose?",
        "choices": {"a":"gold chest","b":"wooden chest"},
        "next": {"a":"trap","b":"treasure"}
    },
        "left_path": {
        "question": "you go left and see what looks like a goblin, what will you do?",
        "choices": {"a":"fight","b":"run"},
        "next": {"a":"fight_goblin","b":"start"}
    },
        "trap": {
        "question": "It was a trap. Game over!",
        "choices": {},
        "next": {}
    },
        "treasure": {
        "question": "You find treasure! Enjoy your life of luxury. You win!",
        "choices": {},
        "next": {}
    },
        "fight_goblin": {
        "question": "You approach the goblin. what now?",
        "choices": {"a":"punch goblin","b":"look for a weapon"},
        "next": {"a":"punch_goblin","b":"weapon_search"}
    },
        "punch_goblin": {
        "question": "You punch the goblin and die for the effort. you lose!",
        "choices": {},
        "next": {}
    },
        "weapon_search": {
        "question": "you look around the cave for some form of weapon, what do you choose?",
        "choices": {"a":"rusty sword","b":"rock"},
        "next": {"a":"rusty_sword","b":"rock_path"}
    },
        "rusty_sword": {
        "question": "You choose the rusty sword and it breaks. You lose!",
        "choices": {},
        "next": {}
    },
        "rock_path": {
        "question": "You choose the rock and successfully scare off the goblin. You win!",
        "choices": {},
        "next": {}
    },
}



question_label = tk.Label(root, text="", wraplength=380)
question_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

end_label = tk.Label(root, text="")
end_label.pack(pady=10)


def ask_question(node_key):
    end_label.config(text="")
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




