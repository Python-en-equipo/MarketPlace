function Contact() {
  return (
    <div>
      <h2 className="text-center text-xl font-bold py-4">Get in touch</h2>
      <section className="py-8 sm:w-[800px] sm:max-w-full mx-auto px-4">
        <h3 className="text-xl font-bold text-center py-4">Custom Service</h3>
        <div className="flex flex-col items-center sm:flex-row sm:justify-between">
          <article className="flex flex-col items-center w-[172px] py-4">
            <h4 className="text-rose-600 pb-2">Flagship Store</h4>
            <p>500 Terry Francisco St</p>
            <p>San Francisco, CA 94158</p>
          </article>
          <article className="flex flex-col items-center w-[172px] py-4">
            <h4 className="text-rose-600 pb-2">Opening Hours</h4>
            <p>Monday-Friday</p>
            <p>9:00am - 7:00pm EST</p>
          </article>
          <article className="flex flex-col items-center w-[172px] py-4">
            <h4 className="text-rose-600 pb-2">Contact Us</h4>
            <p>1-800-000-0000</p>
            <p>info@mysite.com</p>
          </article>
        </div>
        <article className="flex flex-col items-center py-4">
          <h4 className="text-rose-600 py-2">Inquiries</h4>
          <p>for questions regarding our products and services</p>
          <p>you can also contact us by filling out the form below</p>
        </article>
      </section>
      <section className="py-8 flex justify-center sm:w-[800px] max-w-full mx-auto px-4">
        <form className="flex flex-col items-normal w-full ">
          <div className="flex flex-col">
            <input
              className="border-b-2 border-rose-300 p-4"
              name="firstName"
              type="text"
              placeholder="First Name"
            />
            <input
              className="border-b-2 border-rose-300 p-4"
              name="lastName"
              type="text"
              placeholder="Last Name"
            />
          </div>
          <input
            className="border-b-2 border-rose-300 p-4"
            type="email"
            name="email"
            id=""
            placeholder="Email"
          />
          <input
            className="border-b-2 border-rose-300 p-4"
            type="text"
            name=""
            id=""
            placeholder="Subject"
          />
          <textarea
            className="border-b-2 border-rose-300  p-4"
            name="message"
            placeholder="Messages"
            id=""
          ></textarea>
          <input
            className="border-2 border-rose-300 mt-4 p-4"
            type="submit"
            value="Submit"
          />
        </form>
      </section>
    </div>
  );
}

export default Contact;
