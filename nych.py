import streamlit as st
from PIL import Image
import os

def main():
    # Set up page
    st.set_page_config(page_title="New York Chambers", page_icon="🏙️", layout="wide")
    
    # Define correct paths for images
    # Define correct paths for images
    image_folder = "myenv/"  # Adjust if needed
    logo_path = os.path.join(image_folder, "nychamberslogo.webp")
    img1_path = os.path.join(image_folder, "newyorkchambers1.jpeg")
    img2_path = os.path.join(image_folder, "newyorkchambers4.jpeg")
    img3_path = os.path.join(image_folder, "newyorkchambers6.jpeg")

    
    # Load images if they exist
    if os.path.exists(logo_path):
        logo = Image.open(logo_path)
        st.image(logo, width=300)
    else:
        st.warning("Logo image not found.")
    
    # Title and Introduction
    st.title("New York Chambers")
    st.subheader("Where Innovation Meets Industry")
    
    st.write(
        "New York Chambers is a dynamic multi-industry company specializing in **Shipping & Logistics, Civil Engineering, Fashion & Design, and Event Management**. "
        "We take pride in offering state-of-the-art solutions across multiple industries, redefining standards with cutting-edge innovation, exceptional service, and a vision for the future."
    )
    
    st.markdown("---")
    
    # About Section
    st.header("About Us")
    st.write(
        "At New York Chambers, our mission is to push boundaries and create exceptional experiences across industries. "
        "We have a strong global presence with industry-leading professionals dedicated to delivering excellence in logistics, construction, fashion, and luxury event planning."
    )
    
    st.image(img1_path, caption="New York Headquarters")
    
    st.markdown("---")
    
    # Services
    st.header("Our Core Services")
    
    tab1, tab2, tab3, tab4 = st.tabs(["Shipping & Logistics", "Civil Engineering", "Fashion & Design", "Event Management & Party Services"])
    
    with tab1:
        st.subheader("Shipping & Logistics")
        st.image("https://source.unsplash.com/800x400/?ship,container", caption="Global Shipping Solutions")
        st.write(
            "We provide high-quality, **efficient shipping and logistics services** for international and domestic markets. "
            "Our logistics solutions include cargo management, freight forwarding, sustainable transport solutions, and smart tracking technologies."
        )
        st.button("Learn More", key="shipping_btn")
    
    with tab2:
        st.subheader("Civil Engineering & Infrastructure")
        st.image("https://source.unsplash.com/800x400/?construction,bridge", caption="Revolutionizing Infrastructure")
        st.write(
            "Our engineering division specializes in **sustainable infrastructure, smart city development, and large-scale commercial projects**. "
            "We deliver high-quality construction solutions that merge safety, sustainability, and modern technology."
        )
        st.button("Explore Projects", key="engineering_btn")
    
    with tab3:
        st.subheader("Fashion & Design")
        st.image("https://source.unsplash.com/800x400/?fashion,design", caption="Luxury & Sustainable Fashion")
        st.write(
            "Merging craftsmanship with technology, we design **luxury fashion and sustainable apparel**. Our brand focuses on creating high-end streetwear, eco-friendly fabrics, and runway-ready designs."
        )
        st.button("Discover Collection", key="fashion_btn")
    
    with tab4:
        st.subheader("Event Management & Party Services")
        st.image("https://chambers.com/legal-rankings/media-entertainment-advisory-new-york-5:3150:12806:1?l=en-GB", caption="Exclusive Events & Luxury Venues")
        st.write(
            "New York Chambers is a premier provider of **luxury event planning, corporate functions, weddings, private parties, and venue rentals**. "
            "Our event services include:"
        )
        st.markdown(
            "- **Corporate Events**: Conferences, networking events, and executive retreats.\n"
            "- **Luxury Weddings**: Elegant weddings with world-class catering, décor, and entertainment.\n"
            "- **Private Parties**: Birthdays, anniversaries, themed parties, and exclusive VIP gatherings.\n"
            "- **Nightlife & Entertainment**: Live DJs, celebrity performances, and fully customized party experiences.\n"
            "- **Venue Rentals**: High-end venues in prime locations, offering state-of-the-art facilities and stunning aesthetics."
        )
        st.button("Explore Our Events", key="events_btn")
    
    st.markdown("---")
    
    # Contact Information
    st.header("Get in Touch")
    st.write("Reach out to us for inquiries, partnerships, or career opportunities.")
    
    st.info(
        """**Email:** newyorkchambers@workmail.com  
        **Phone:** +1 (617) 470-1135  
        **Address:** 403 East 68th Street, New York, NY 10001  
        **Follow us on:** [LinkedIn](https://www.linkedin.com) | [Twitter](https://twitter.com) | [Instagram](https://instagram.com)"""
    )
    
    # Contact Form
    st.header("Send Us a Message")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send Message")
        
        if submitted:
            st.success(f"Thank you, {name}! Your message has been received.")
    
    # Additional Image
    if os.path.exists(img2_path):
        st.image(img2_path, caption="Our Team at Work", use_container_width=True)
    else:
        st.warning("Image 2 not found.")
    
    # Footer
    st.markdown("---")
    st.write("© 2025 New York Chambers. All rights reserved.")

if __name__ == "__main__":
    main()

#streamlit run .\myenv\nychambers.py
