import random
from pyscript import document, when
from questions import QUESTIONS

def shuffle(lst):
    for i in range(len(lst) - 1, 0, -1):
        j = random.randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]

shuffle(QUESTIONS)

state = {"i": 0, "score": 0, "answered": False}

def el(id):
    return document.getElementById(id)

def show():
    i = state["i"]
    state["answered"] = False
    el("result").innerText = ""
    el("explain").innerText = ""
    el("next").hidden = True
    if i >= len(QUESTIONS):
        el("count").innerText = ""
        el("question").innerText = "終了！ 得点: %d / %d" % (state["score"], len(QUESTIONS))
        el("maru").hidden = True
        el("batsu").hidden = True
        return
    el("count").innerText = "第%d問 / 全%d問"% (i + 1, len(QUESTIONS))
    el("question").innerText = "次の文章は〇か×か。" + QUESTIONS[i]["text"]

def answer(choice):
    if state["answered"]:
        return
    state["answered"] = True
    q = QUESTIONS[state["i"]]
    if choice == q["answer"]:
        state["score"] += 1
        el("result").innerText = "正解！"
    else:
        el("result").innerText = "不正解..."
    el("explain").innerText = "解説: " + q["explain"]
    el("next").hidden = False

@when("click", "#maru")
def on_maru(event):
    answer(True)

@when("click", "#batsu")
def on_batsu(event):
    answer(False)

@when("click", "#next")
def on_next(event):
    state["i"] += 1
    show()

show()