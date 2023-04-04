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
        a = st.number_input("Enter a", value = 0.0)
        b = st.number_input("Enter b", value = 0.0)

        choice = st.radio('Pick one', ['Iteration', 'Error'])
        if choice == 'Iteration':
            count = 2
            error = st.number_input("Enter Iterations", min_value=1)
            st.write("Entered Values:")
            st.write("A = ", a)
            st.write("B = ", b)
            st.write("Iterations = ", error)
            c = (a+b)/2
            d = math.tanh(c)
            e = abs(a-b)
            data = {
                "a": [a], "b": [b], "c": [c], "f(c)": [d], "|a-b|": [e],
            }
            df = pd.DataFrame(data)

            while count <= error:
                if (math.tanh(a))*d > 0:
                    a = c
                elif (math.tanh(b))*d > 0:
                    b = c

                count += 1
                c = (a+b)/2
                d = math.tanh(c)
                e = abs(a-b)

                new_row = {'a': a, 'b': b, 'c': c, 'f(c)': d, '|a-b|':[e]}
                df = pd.concat([df, pd.DataFrame(new_row)])

            st.write("---")
            st.subheader("Answers")
            st.write("Cn= ", c)
            st.write("f(Cn)= ", d)

            # Display the dataframe in a table
            st.write("---")
            st.write("Table:")
            df.index = np.arange(1, len(df) + 1)
            st.table(df)
            st.markdown("<span style='color:green'>Note: <br>the table can only show values up to 4 decimal places</span>", unsafe_allow_html=True)


        else:
            error = st.number_input("Enter error", value = 0.01)
            st.write("Entered Values:")
            st.write("A = ", a)
            st.write("B = ", b)
            st.write("Error = ", error)
            c = (a+b)/2
            d = math.tanh(c)
            e = abs(a-b)
            data = {
                "a": [a], "b": [b], "c": [c], "f(c)": [d], "|a-b|": [e],
            }
            df = pd.DataFrame(data)

            while error <= e:
                if (math.tanh(a))*d > 0:
                    a = c
                elif (math.tanh(b))*d > 0:
                    b = c

                c = (a+b)/2
                d = math.tanh(c)
                e = abs(a-b)

                new_row = {'a': a, 'b': b, 'c': c, 'f(c)': d, '|a-b|':[e]}
                df = pd.concat([df, pd.DataFrame(new_row)])

            st.write("---")
            st.subheader("Answers")
            st.write("Cn= ", c)
            st.write("f(Cn)= ", d)

            # Display the dataframe in a table
            st.write("---")
            st.write("Table:")
            df.index = np.arange(1, len(df) + 1)
            
            st.table(df)

            st.markdown("<span style='color:green'>Note: <br>the table can only show values up to 4 decimal places</span>", unsafe_allow_html=True)


    with tab2:
        st.title("Secant Method")
        st.text("Function: tanh(x)")

        a = st.number_input("Enter X₀", value = 2, min_value=-2, max_value=2)
        b = st.number_input("Enter X₁", value=1, min_value=-2, max_value=2)
        st.markdown("<span style='color:red'>0 as an input for X₁ will not work on tanh(x) </span>", unsafe_allow_html=True)
        while abs(float(b)) == abs(float(a)):
            st.warning("Inputs should not be equal to the absolute value of each other")
            b = st.number_input("Enter X₁", value=1, min_value=-2, max_value=2)
        while (float(b)) == 0.0 or float(a) == 0:
            st.warning("Please enter a non-zero value.")
            b = st.number_input("Enter X₁", value=1, min_value=-2, max_value=2)


        choice = st.radio('Pick one ', ['Iteration', 'Error'])
        if choice == 'Iteration':
                count = 2
                error = st.number_input("Enter error ", value = 1)
                st.write("Entered Values:")
                st.write("A = ", a)
                st.write("B = ", b)
                st.write("Iterations = ", error)
                c = math.tanh(a)    
                d = math.tanh(b)
                e = (b - ((d)*(b-a)/(d-c)))
                f = abs(e-b)
                data = {
                    "Xi-1": [a], "Xi": [b], "f(Xi-1)": [c], "f(Xi)": [d], "Xi+1": [e], "|Xi+1 - Xi|": [f],
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

                    new_row = {'Xi-1': a, 'Xi': b, 'f(Xi-1)': c, 'f(Xi)': d, 'Xi+1': e, '|Xi+1 - Xi|': [f]}
                    df = pd.concat([df, pd.DataFrame(new_row)])

                st.write("---")
                st.subheader("Answers")
                st.write("Cn= ", e)
                st.write("f(Cn)= ", math.tanh(e))

                # Display the dataframe in a table
                st.write("---")
                st.write("Table:")
                df.index = np.arange(1, len(df) + 1)
                st.table(df)
                st.markdown("<span style='color:green'>Note: <br>the table can only show values up to 4 decimal places</span>", unsafe_allow_html=True)


        else:
            error = st.number_input("Enter error ",min_value=0.00001 , step=1e-5, format="%.5f")
            st.write("Entered Values:")
            st.write("A = ", a)
            st.write("B = ", b)
            st.write("Error = ", error)
            c = math.tanh(a)    
            d = math.tanh(b)
            e = (b - ((d)*(b-a)/(d-c)))
            f = abs(e-b)
            data = {
                "Xi-1": [a], "Xi": [b], "f(Xi-1)": [c], "f(Xi)": [d], "Xi+1": [e], "|Xi+1 - Xi|": [f],
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

                new_row = {'Xi-1': a, 'Xi': b, 'f(Xi-1)': c, 'f(Xi)': d, 'Xi+1': e, '|Xi+1 - Xi|': [f]}
                df = pd.concat([df, pd.DataFrame(new_row)])

            st.write("---")
            st.subheader("Answers")
            st.write("Cn= ", e)
            st.write("f(Cn)= ", math.tanh(e))

            # Display the dataframe in a table
            st.write("---")
            st.write("Table:")
            df.index = np.arange(1, len(df) + 1)
            st.table(df)
            st.markdown("<span style='color:green'>Note: <br>the table can only show values up to 4 decimal places</span>", unsafe_allow_html=True)


if __name__ == '__main__':
    main()
