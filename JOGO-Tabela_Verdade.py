import itertools
import random
import tkinter as tk
from tkinter import messagebox, scrolledtext, simpledialog


# Definições das proposições lógicas
def não_op(p):
    return not p

def e_op(p, q):
    return p and q

def ou_op(p, q):
    return p or q

def implicação_op(p, q):
    return not p or q

def bi_implicação_op(p, q):
    return p == q

# Função para gerar todas as combinações de valores de verdade para proposições
def generate_truth_values(n):
    return list(itertools.product([True, False], repeat=n))

# Função para calcular a tabela-verdade de uma proposição
def calculate_truth_table(variables, expression):
    table = []
    values = generate_truth_values(len(variables))
    env_functions = {
        "não_op": não_op,
        "e_op": e_op,
        "ou_op": ou_op,
        "implicação_op": implicação_op,
        "bi_implicação_op": bi_implicação_op
    }
    for val in values:
        env = dict(zip(variables, val))
        env.update(env_functions)
        result = eval(expression, {}, env)
        table.append((val, result))
    return table

# Função para formatar a tabela-verdade
def format_truth_table(variables, table, show_result=False):
    header = " | ".join(variables) + " | Resultado"
    rows = [header, "-" * len(header)]
    for row in table:
        values = " | ".join('V' if v else 'F' for v in row[0])
        result = 'V' if row[1] else 'F' if show_result else '?'
        rows.append(f"{values} |   {'?' if not show_result else result}")
    return rows

# Função principal do jogo
def truth_table_game():
    root = tk.Tk()
    root.withdraw()

    def new_game():
        proposition = random.choice(propositions)
        correct_table = calculate_truth_table(variables, proposition)
        table_str = "\n".join(format_truth_table(variables, correct_table, show_result=False))

        new_window = tk.Toplevel(root)
        new_window.title('Jogo da Tabela-Verdade')

        tk.Label(new_window, text='Calcule a tabela-verdade para a proposição:').pack()
        tk.Label(new_window, text=proposition.replace("_op", "")).pack()
        tk.Label(new_window, text='Tabela-verdade:').pack()

        table_text = scrolledtext.ScrolledText(new_window, width=40, height=10, state='normal')
        table_text.insert(tk.END, table_str)
        table_text.configure(state='disabled')
        table_text.pack()

        tk.Label(new_window, text='Insira os resultados (V para verdadeiro, F para falso):').pack()
        input_entries = []
        for i in range(len(correct_table)):
            entry = tk.Entry(new_window, width=5)
            entry.pack()
            input_entries.append(entry)

        def verificar():
            user_answers = []
            try:
                for i in range(len(correct_table)):
                    answer = input_entries[i].get().upper()
                    if answer in ['V', 'F']:
                        user_answers.append((correct_table[i][0], answer == 'V'))
                    else:
                        raise ValueError
                correct_count = sum(1 for a, b in zip(correct_table, user_answers) if a == b)
                total = len(correct_table)
                result_message = f"Você acertou {correct_count} de {total} linhas."
                if correct_count == total:
                    result_message += "\nParabéns! Você completou a tabela-verdade corretamente."
                else:
                    result_message += "\nVeja a tabela-verdade correta abaixo:\n" + "\n".join(format_truth_table(variables, correct_table, show_result=True))
                messagebox.showinfo("Resultado", result_message)
                
                play_again = messagebox.askyesno("Jogar novamente?", "Você quer jogar novamente?")
                if play_again:
                    new_window.destroy()
                    new_game()
                else:
                    root.destroy()
            except ValueError:
                messagebox.showerror("Erro", "Por favor, insira V ou F em todos os campos.")

        tk.Button(new_window, text='Verificar', command=verificar).pack()
        tk.Button(new_window, text='Sair', command=root.destroy).pack()

    propositions = ["não_op(p)", "e_op(p, q)", "ou_op(p, q)", "implicação_op(p, q)", "bi_implicação_op(p, q)"]
    variables = ['p', 'q']

    new_game()
    root.mainloop()

if __name__ == "__main__":
    truth_table_game()
