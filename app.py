
import streamlit as st

# Custom title and subtitle matching your opening text
st.title("🚭 Testrun2")
st.caption("'The secret of getting ahead is getting started!'")
st.write("Thank you for selecting testrun2. Let us get started with getting along.")

# 1. Ask for their name
name = st.text_input("What is your name?")

# Only show the rest of the app once they've entered a name
if name:
    st.write(f"### Nice to meet you, {name}!")
    st.write("Only one thing to know before getting started...")
    
    # 2. Ask for CPD using a visual number input box
    y = st.number_input("What is your CPD (Cigarettes Per Day)?", min_value=0, max_value=100, step=1, value=0)
    
    # Only run the checks if they actually smoke 1 or more cigarettes
    if y > 0:
        st.markdown("---") # Visual divider line
        
        # 3. Your exact conditional logic translated to web text alerts
        if 1 <= y <= 5:
            st.error("The cigarette does not relieve stress.")
            st.info("It temporarily relieves the nicotine withdrawal that the previous cigarette created.")
            
        elif 6 <= y <= 10:
            st.error("The moment you throw away your last pack you are not giving up a friend.")
            st.success("You are executing a prison break.")
            
        elif 11 <= y <= 15:
            st.error("A cigarette is a pipe with a fire at one end and a fool at the other.")
            
        elif 16 <= y <= 20:
            st.error("There is no such thing as just one cigarette.")
            st.warning("One always leads back to the whole pack.")
            
        elif y >= 21:
            st.error("Seeking our help means you know you want to quit.")
            st.warning("Take professional medical help immediately.")
            st.info("It is never too late!")
            
        st.markdown("---")
        st.subheader("Do not smoke your future away. Your health is the only true wealth you have!")
        st.caption("#quitsmoking")
