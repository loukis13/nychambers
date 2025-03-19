import streamlit as st
from PIL import Image

def main():
    # Set up page
    st.set_page_config(page_title="New York Chambers", page_icon="🏙️", layout="wide")
    
    # Title and Introduction
    st.title("New York Chambers")
    st.subheader("Where Innovation Meets Industry")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("https://source.unsplash.com/800x400/?newyork,city", caption="New York Headquarters")
    with col2:
        st.write(
            "New York Chambers is an innovative firm at the intersection of **shipping, civil engineering, and fashion**. "
            "With headquarters in New York, we redefine industry standards by merging technology and creativity to build a sustainable future."
        )
    
    st.markdown("---")
    
    # Services
    st.header("Our Core Services")
    
    tab1, tab2, tab3 = st.tabs(["Shipping", "Civil Engineering", "Fashion"])
    
    with tab1:
        st.subheader("Shipping & Logistics")
        st.image("https://source.unsplash.com/800x400/?ship,container", caption="Global Shipping Solutions")
        st.write(
            "We provide cutting-edge shipping and logistics solutions, including cargo management, international trade consulting, "
            "and sustainable shipping technologies. Our expertise ensures efficient and secure transport across global markets."
        )
    
    with tab2:
        st.subheader("Civil Engineering & Infrastructure")
        st.image("https://source.unsplash.com/800x400/?construction,bridge", caption="Revolutionizing Infrastructure")
        st.write(
            "Our civil engineering division specializes in large-scale infrastructure projects, smart cities, and sustainable development. "
            "From designing state-of-the-art skyscrapers to reinforcing critical infrastructure, we drive engineering excellence."
        )
    
    with tab3:
        st.subheader("Fashion & Design")
        st.image("https://source.unsplash.com/800x400/?fashion,design", caption="Redefining Luxury Fashion")
        st.write(
            "Merging craftsmanship with technology, our fashion division creates luxury and sustainable apparel. "
            "From high-end streetwear to eco-friendly fabrics, we redefine style with innovation."
        )
    
    st.markdown("---")
    
    # Contact Information
    st.header("Get in Touch")
    st.write("Reach out to us for inquiries, partnerships, or career opportunities.")
    
    st.info(
        "**Email:** newyorkchambers@gmail.com  
        **Phone:** +1 (617) 470-1135  
        **Address:** 123 Innovation Avenue, New York, NY 10001  
        **Follow us on:** [LinkedIn](https://www.linkedin.com) | [Twitter](https://twitter.com) | [Instagram](https://instagram.com)"
    )
    
    # Contact Form
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send Message")
        
        if submitted:
            st.success(f"Thank you, {name}! Your message has been received.")
    
    # Footer
    st.markdown("---")
    st.write("© 2025 New York Chambers. All rights reserved.")

if __name__ == "__main__":
    main()
