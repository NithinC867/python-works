user_input="{[]}"
symbol_table={
        "<":">",
        "[":"]",
        "(":")",
        "{":"}"
    }
top=-1
symbol_stack=[]
is_valid="valid"
for symbol in user_input:
    if symbol in symbol_table:
        top+=1
        symbol_stack.append(symbol)
    else:
        current_symbol=symbol_stack[top]
        current_symbol_closing=symbol_table[current_symbol]
        if symbol==current_symbol_closing:
            symbol_stack.pop()
            top-=1
        else:
            is_valid="not valid"
            break
print(is_valid)
if len(symbol_stack)!=0:
    print("not valid")