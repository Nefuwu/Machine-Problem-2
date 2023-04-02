import streamlit as st
import pandas as pd
import numpy as np
import math

st.set_page_config(page_title="Bisection Method Table", page_icon=":memo:")


def main():
    tab1, tab2 = st.tabs(["Bisection", "Secant"])
    with tab1:
        st.title("Bisection Method")
        st.text("Function: tanh(x)")
        a = st.number_input("Enter a", value = 0)
        b = st.number_input("Enter b", value = 0)

        choice = st.radio('Pick one', ['Iteration', 'Error'])
        if choice == 'Iteration':
            count = 2
            error = st.number_input("Enter error", value = 1)
            c = (a+b)/2
            d = math.tanh(c)
            e = abs(a-b)
            data = {
                "a": [a],
                "b": [b],
                "c": [c],
                "d": [d],
                "e": [e],
            }
            df = pd.DataFrame(data)

            while count <= error:
                if d < 0:
                    b = c
                else:
                    a = c

                count += 1
                c = (a+b)/2
                d = math.tanh(c)
                e = abs(a-b)

                new_row = {'a': a, 'b': b, 'c': c, 'd': d, 'e':[e]}
                df = pd.concat([df, pd.DataFrame(new_row)])

            st.write("---")
            st.write("Cn= ", c)
            st.write("f(Cn)= ", d)

            # Display the dataframe in a table
            st.write("---")
            st.write("Table:")
            df.index = np.arange(1, len(df) + 1)
            st.write(df)

        else:
            error = st.number_input("Enter error", value = 0.01)
            c = (a+b)/2
            d = math.tanh(c)
            e = abs(a-b)
            data = {
                "a": [a],
                "b": [b],
                "c": [c],
                "d": [d],
                "e": [e],
            }
            df = pd.DataFrame(data)

            while error <= e:
                if d < 0:
                    b = c
                else:
                    a = c

                c = (a+b)/2
                d = math.tanh(c)
                e = abs(a-b)

                new_row = {'a': a, 'b': b, 'c': c, 'd': d, 'e':[e]}
                df = pd.concat([df, pd.DataFrame(new_row)])

            st.write("---")
            st.write("Cn= ", c)
            st.write("f(Cn)= ", d)

            # Display the dataframe in a table
            st.write("---")
            st.write("Table:")
            df.index = np.arange(1, len(df) + 1)
            st.write(df)


    with tab2:
        st.title("Secant Method")
        st.text("Function: tanh(x)")

        a = st.number_input("Enter X₀", min_value=1)
        b = st.number_input("Enter X₁", min_value=0.00001)

        choice = st.radio('Pick one ', ['Iteration', 'Error'])
        if choice == 'Iteration':
                count = 2
                error = st.number_input("Enter error ", value = 1)
                c = math.tanh(a)    
                d = math.tanh(b)
                e = (b - ((d)*(b-a)/(d-c)))
                f = abs(e-b)
                data = {
                    "a": [a],
                    "b": [b],
                    "c": [c],
                    "d": [d],
                    "e": [e],
                    "f": [f],
                }
                df = pd.DataFrame(data)

                while count <= error:
                    tempa = b
                    tempb = e

                    a = tempa
                    b = tempb
                    count += 1
                    c = math.tanh(a)
                    d = math.tanh(b)
                    e = b - ((d)*(b-a)/(d-c))
                    f = abs(e-b)

                    new_row = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': [f]}
                    df = pd.concat([df, pd.DataFrame(new_row)])

                st.write("---")
                st.write("Cn= ", c)
                st.write("f(Cn)= ", d)

                # Display the dataframe in a table
                st.write("---")
                st.write("Table:")
                df.index = np.arange(1, len(df) + 1)
                st.write(df)

        else:
            error = st.number_input("Enter error ", min_value=0.00001, max_value=1.0, step=1e-5, format="%.5f")
            c = math.tanh(a)    
            d = math.tanh(b)
            e = (b - ((d)*(b-a)/(d-c)))
            f = abs(e-b)
            data = {
                "a": [a],
                "b": [b],
                "c": [c],
                "d": [d],
                "e": [e],
                "f": [f],
            }
            df = pd.DataFrame(data)

            while error <= f:
                tempa = b
                tempb = e

                a = tempa
                b = tempb
                c = math.tanh(a)
                d = math.tanh(b)
                e = b - ((d)*(b-a)/(d-c))
                f = abs(e-b)

                new_row = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': [f]}
                df = pd.concat([df, pd.DataFrame(new_row)])

            st.write("---")
            st.write("Cn= ", c)
            st.write("f(Cn)= ", d)

            # Display the dataframe in a table
            st.write("---")
            st.write("Table:")
            df.index = np.arange(1, len(df) + 1)
            st.write(df)

        
if __name__ == '__main__':
    main()
