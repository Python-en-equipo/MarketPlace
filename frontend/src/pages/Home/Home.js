import Carousel from "../../components/Carusel";

import background from "../../assets/img/media/background.jpg";
import img1 from "../../assets/img/media/mano.jpg";
import img2 from "../../assets/img/media/bolso.webp";
import img3 from "../../assets/img/media/img3.jpg";
import img4 from "../../assets/img/media/correo.webp";
import card1 from "../../assets/img/media/card1.jpg";
import card2 from "../../assets/img/media/card2.jpg";
import card3 from "../../assets/img/media/card3.jpg";

const Home = () => {
  return (
    <>
      <section className="w-screen min-h-screen relative left-0 overflow-x-hidden">
        {/* HOME - FIRST SECTION (IMG AND TITLE) */}
        <div
          className="background w-screen h-screen grid place-content-center"
          style={{ 
            backgroundImage: `url(${background})`,  
            backgroundSize: "cover",
            backgroundPosition: "50% 50%",
            backgroundRepeat: "no-repeat",
            backgroundAttachment:"fixed" }}
        >
          <p className="text-white text-center">
            <h1 className="font-bold text-5xl tracking-widest align-middle">
              CUE THE COLOR
            </h1>
            <button className="border-2 border-white my-4 py-5 px-16 transition-colors duration-[0.4s] hover:bg-white hover:text-red-500 text-xl">
              Shop the collection
            </button>
          </p>
        </div>
        {/* HOME - SECOND SECTION (SLIDER) */}
        <div className="w-screen h-screen grid place-content-center">
          <Carousel/>
        </div>
        {/* HOME - THIRT SECTION (PRODUCT PUBLICITY) */}
        <div className="w-screen min-h-screen flex flex-wrap text-center flex-shrink-0">
          <div className="relative w-screen sm:w-1/2 min-h-[450px] max-h-[600px] grid place-content-center text-center text-gray-700 bg-white group">
            <figure>
              <img
                src={img2}
                alt="bolso"
                className="group-hover:animate-pulse"
              />
            </figure>
            <p className="h-20">
              <span className="text-lg leading-[2] opacity-100 group-hover:opacity-0 transition-opacity duration-300">
                Im a product <br />{" "}
                <span className="text-orange-500 italic">$100.00</span>
              </span>
              <a
                href=""
                className="absolute w-1/2 p-3 border-2 border-orange-500 bottom-8 left-1/2 -translate-x-1/2  opacity-0 group-hover:opacity-100 text-red-500 hover:text-orange-500 border-red-500 hover:border-orange-500 transition-opacity duration-300"
              >
                Add to cart
              </a>
            </p>
          </div>
          <div
            className="relative w-screen sm:w-1/2 min-h-[450px] max-h-[600px] grid place-content-center parallax2"
            style={{ backgroundImage: `url(${img1})`,backgroundBlendMode:'darken', backgroundColor:'rgba(0,0,0,0.1'}}
          >
              <a className="text-2xl text-white underline tracking-wider">
                MINI LEATHER GOODS
              </a>
          </div>
          <div
            className="relative w-screen sm:w-1/2 min-h-[450px] max-h-[600px] grid place-content-center background2"
            style={{
              backgroundImage: `url(${img3})`,
              backgroundSize: "cover",
              backgroundPosition: "50% 50%",
              backgroundRepeat: "no-repeat",
            }}
          >
            <a href="" className="text-2xl text-white underline tracking-wider">
              LEATHER BELTS
            </a>
          </div>
          <div className="relative w-screen sm:w-1/2 min-h-[450px] max-h-[600px] grid place-content-center bg-white group">
            <figure>
              <img
                src={img4}
                alt="correa"
                className="group-hover:animate-pulse transition-all duration-300"
              />
            </figure>
            <p className="h-20">
              <span className="text-lg leading-[2] opacity-100 group-hover:opacity-0 transition-opacity duration-300">
                Im a product <br />{" "}
                <span className="text-orange-500 italic">$100.00</span>
              </span>
              <a
                href=""
                className="absolute w-1/2 p-3 border-2 border-orange-500 left-1/2 bottom-8 -translate-x-1/2   opacity-0 group-hover:opacity-100 text-red-500 hover:text-orange-500 border-red-500 hover:border-orange-500 transition-opacity duration-300"
              >
                Add to cart
              </a>
            </p>
          </div>
        </div>    
        {/* HOME - FOURTH SECTION (CARDS) */}
        <div className="w-screen min-h-screen flex items-center justify-center">
          <div className="w-full grid grid-cols-[repeat(auto-fit,minmax(280px,1fr))] auto-rows-[450px] gap-7 sm:gap-14 p-0 xsm:p-6 sm:p-14 text-center">
            <div
              className="relative bg-no-repeat bg-cover text-white"
              style={{ backgroundImage: `url(${card1})` }}
            >
              <p className="w-full h-full grid place-content-center bg-[rgba(0,0,0,0.3)]">
                <span
                  className="text-2xl leading-[2]"
                  style={{
                    fontFamily: "didot-w02-italic,serif",
                    fontStyle: "oblique",
                  }}
                  href=""
                >
                  Family Owned
                </span>
                <span className="relative uppercase font-bold text-3xl before:w-8 before:h-1 before:bg-white before:absolute before:-bottom-3 before:left-1/2 before:-translate-x-1/2">
                  Brand
                </span>
                <a href="" className="underline mt-6">
                  link
                </a>
              </p>
            </div>
            <div
              className="relative bg-no-repeat bg-cover text-white"
              style={{ backgroundImage: `url(${card2})` }}
            >
              <p className="w-full h-full grid place-content-center bg-[rgba(0,0,0,0.3)]">
                <span
                  className="text-2xl leading-[2]"
                  style={{
                    fontFamily: "didot-w02-italic,serif",
                    fontStyle: "oblique",
                  }}
                  href=""
                >
                  Hand Crafted
                </span>
                <span className="relative uppercase font-bold text-3xl before:w-8 before:h-1 before:bg-white before:absolute before:-bottom-3 before:left-1/2 before:-translate-x-1/2">
                  Products
                </span>
                <a href="" className="underline mt-6">
                  link
                </a>
              </p>
            </div>
            <div
              className="relative bg-no-repeat bg-cover text-white"
              style={{ backgroundImage: `url(${card3})` }}
            >
              <p className="w-full h-full grid place-content-center bg-[rgba(0,0,0,0.3)]">
                <span
                  className="text-2xl leading-[2]"
                  style={{
                    fontFamily: "didot-w02-italic,serif",
                    fontStyle: "oblique",
                  }}
                  href=""
                >
                  Created in the
                </span>
                <span className="relative uppercase font-bold text-3xl before:w-8 before:h-1 before:bg-white before:absolute before:-bottom-3 before:left-1/2 before:-translate-x-1/2">
                  USA
                </span>
                <a href="" className="underline mt-6">
                  link
                </a>
              </p>
            </div>
          </div>
        </div>
        {/* HOME - FINAL SECTION (TWITTER AND IMAGES CARUSEL) */}
        <div className="w-screen min-h-screen">
          <div className="text-center text-2xl tracking-[0.2em] font-bold w-full h-[250px] flex flex-col items-center justify-center">
            FOLLOW
            <br /> ADALENE ON INSTAGRAM
            <span
              className="tracking-normal text-[#B04828] font-thin"
              style={{
                fontFamily: "didot-w02-italic,serif",
                fontStyle: "oblique",
              }}
            >
              @adaleneshop
            </span>
          </div>
        </div>
      </section>
    </>
  );
};

export default Home;
