function Product() {
  return (
    <div className=" flex flex-col lg:flex-row">
      <section className=" border-black/20 border-b-2 lg:border-b-0 lg:border-r-2 px-4 lg:w-1/2">
        <article className="flex h-96 overflow-hidden ">
          <div className="mx-1.5 flex flex-col gap-2 shrink-0 ">
            <img
              className=" w-24 min-h-0 object-cover"
              src="https://images.unsplash.com/photo-1506898667547-42e22a46e125?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1412&q=80"
              alt=""
            />
            <img
              className=" w-24 min-h-0 object-cover"
              src="https://images.unsplash.com/photo-1506898667547-42e22a46e125?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1412&q=80"
              alt=""
            />
            <img
              className=" w-24 min-h-0 object-cover"
              src="https://images.unsplash.com/photo-1506898667547-42e22a46e125?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1412&q=80"
              alt=""
            />
            <img
              className=" w-24 min-h-0 object-cover"
              src="https://images.unsplash.com/photo-1506898667547-42e22a46e125?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1412&q=80"
              alt=""
            />
          </div>
          <div className="w-full flex">
            <img
              className="w-full object-contain"
              src="https://images.unsplash.com/photo-1506898667547-42e22a46e125?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1412&q=80"
              alt=""
            />
          </div>
        </article>

        <article>
          <header className="flex justify-between p-1.5 font-semibold">
            <p>Recently</p> <span></span> <span></span>
          </header>
          <section className="flex">
            <article className="m-1.5">
              <img
                className="h-24 w-24 object-cover"
                src="https://images.unsplash.com/photo-1506898667547-42e22a46e125?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1412&q=80"
                alt=""
              />
              <footer>
                <small className="text-xs">
                  Product <span className="font-semibold">$300.00</span>
                </small>
              </footer>
            </article>
            <article className="m-1.5">
              <img
                className="h-24 w-24 object-cover"
                src="https://images.unsplash.com/photo-1506898667547-42e22a46e125?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1412&q=80"
                alt=""
              />
              <footer>
                <small className="text-xs">
                  Product <span className="font-semibold">$300.00</span>
                </small>
              </footer>
            </article>
            <article className="m-1.5">
              <img
                className="h-24 w-24 object-cover"
                src="https://images.unsplash.com/photo-1506898667547-42e22a46e125?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1412&q=80"
                alt=""
              />
              <footer>
                <small className="text-xs">
                  Product <span className="font-semibold">$300.00</span>
                </small>
              </footer>
            </article>
          </section>
        </article>
      </section>

      <section className="lg:w-1/2 px-4">
        <h2 className="text-3xl font-semibold">Product</h2>
        <article>
          <p className="py-5">
            A sectional sofa or an L shaped sofa can make a great addition on
            your living room based on your needs
          </p>
          <div>
            <span className="text-xl font-semibold">$430.99</span>
            <div className="flex">
              <div>
                <span>1</span>
                <span>2</span>
                <span>3</span>
                <span>4</span>
                <span>5</span>
              </div>
              <p className="px-1.5">441 reviews</p>
            </div>
          </div>
          <div>
            <div
              className="py-5
          "
            >
              <p className="pb-2">Colour</p>
              <div className="flex gap-4">
                <input
                  className="appearance-none cursor-pointer rounded-full w-12 h-12 bg-yellow-400 checked:border-2 border-gray-500"
                  type="radio"
                  name="color"
                  value="1"
                ></input>
                <input
                  className="appearance-none cursor-pointer rounded-full w-12 h-12 bg-orange-400 checked:border-2 border-gray-500"
                  type="radio"
                  name="color"
                  value="2"
                ></input>
                <input
                  className="appearance-none cursor-pointer rounded-full w-12 h-12 bg-sky-400 checked:border-2 border-gray-500"
                  type="radio"
                  name="color"
                  value="3"
                ></input>
                <input
                  className="appearance-none cursor-pointer rounded-full w-12 h-12 bg-black checked:border-2 border-gray-500"
                  type="radio"
                  name="color"
                  value="4"
                ></input>
              </div>
            </div>
          </div>
          <div className="flex gap-5 lg:gap-0 lg:justify-between">
            <button className="w-52 px-10 py-4 bg-stone-50 border-2 border-black">
              Buy now
            </button>
            <button className="w-52 text-white px-10 py-4 bg-stone-800 border-2 border-stone-800">
              Add to bascket
            </button>
          </div>
        </article>
        <article>
          <div className="py-4 border-b-2 border-gray-200">
            <p>
              Dispatched in 5-7 weeks <span>¡</span>
            </p>
            <p>Why the longer lead time?</p>
          </div>
          <div className="py-4 border-b-2 border-gray-200">
            <p>Home Delivery - $10</p>
          </div>
        </article>
      </section>
    </div>
  );
}

export default Product;
