import {useRef} from "react";
import img1 from "../assets/img/media/03.jpg";
const Carousel = () => {
  const carusel = useRef(null)
  const moveSlidertoLeft = () =>{
    const caruselE = carusel.current
    caruselE.scrollLeft += -Math.floor((caruselE.clientWidth)/2);
  }
  const moveSlidertoRight = () =>{
    const caruselE = carusel.current
    caruselE.scrollLeft += Math.floor((caruselE.clientWidth)/2);
  }
  return (
    <section>
      <div className="w-screen flex relative justify-between items-center">
        <button aria-label="Siguiente" className="block text-black px-3 text-3xl" onClick={() =>moveSlidertoLeft()}>
          <i className="fas fa-chevron-left"></i>
        </button>
      <div className="max-w-[80%] lg:max-w-[93%] h-[26rem] relative left-0">
        <div className="min-w-full h-full overflow-x-scroll flex flex-nowrap gap-16 sm:gap-12 px-6 py-3 scroll transition-all duration-300 scroll-smooth" ref={carusel}>
          <div className="relative min-w-[230px] sm:min-w-[250px] max-w-[280px] h-full after:absolute after:top-0 after:left-0 after:w-32 after:h-8 after:bg-red-500 after:text-white after:content-['Best_Seller'] after:text-xl after:py-1 after:text-center">
            <img src={img1} className="mb-6" alt="product"/>
            <p className="text-xl text-center mb-3">
            <span style={{fontFamily:'didot-w02-italic,serif',fontWeight:200}}>Im a product</span>
            </p>
            <p className="text-lg text-center">
            <span className="text-light-orange italic pt-4">$100.00</span>
            </p>
          </div>
          <div className="relative min-w-[230px] sm:min-w-[250px] max-w-[280px] h-full after:absolute after:top-0 after:left-0 after:w-32 after:h-8 after:bg-red-500 after:text-white after:content-['Best_Seller'] after:text-xl after:py-1 after:text-center">
            <img src={img1} className="mb-6" alt="product"/>
            <p className="text-xl text-center mb-3">
            <span style={{fontFamily:'didot-w02-italic,serif',fontWeight:200}}>Im a product</span>
            </p>
            <p className="text-lg text-center">
            <span className="text-light-orange italic pt-4">$100.00</span>
            </p>
          </div>
          <div className="relative min-w-[230px] sm:min-w-[250px] max-w-[280px] h-full after:absolute after:top-0 after:left-0 after:w-32 after:h-8 after:bg-red-500 after:text-white after:content-['Best_Seller'] after:text-xl after:py-1 after:text-center">
            <img src={img1} className="mb-6" alt="product"/>
            <p className="text-xl text-center mb-3">
            <span style={{fontFamily:'didot-w02-italic,serif',fontWeight:200}}>Im a product</span>
            </p>
            <p className="text-lg text-center">
            <span className="text-light-orange italic pt-4">$100.00</span>
            </p>
          </div>
          <div className="relative min-w-[230px] sm:min-w-[250px] max-w-[280px] h-full after:absolute after:top-0 after:left-0 after:w-32 after:h-8 after:bg-red-500 after:text-white after:content-['Best_Seller'] after:text-xl after:py-1 after:text-center">
            <img src={img1} className="mb-6" alt="product"/>
            <p className="text-xl text-center mb-3">
            <span style={{fontFamily:'didot-w02-italic,serif',fontWeight:200}}>Im a product</span>
            </p>
            <p className="text-lg text-center">
            <span className="text-light-orange italic pt-4">$100.00</span>
            </p>
          </div>
          <div className="relative min-w-[230px] sm:min-w-[250px] max-w-[280px] h-full after:absolute after:top-0 after:left-0 after:w-32 after:h-8 after:bg-red-500 after:text-white after:content-['Best_Seller'] after:text-xl after:py-1 after:text-center">
            <img src={img1} className="mb-6" alt="product"/>
            <p className="text-xl text-center mb-3">
            <span style={{fontFamily:'didot-w02-italic,serif',fontWeight:200}}>Im a product</span>
            </p>
            <p className="text-lg text-center">
            <span className="text-light-orange italic pt-4">$100.00</span>
            </p>
          </div>
          <div className="relative min-w-[230px] sm:min-w-[250px] max-w-[280px] h-full after:absolute after:top-0 after:left-0 after:w-32 after:h-8 after:bg-red-500 after:text-white after:content-['Best_Seller'] after:text-xl after:py-1 after:text-center">
            <img src={img1} className="mb-6" alt="product"/>
            <p className="text-xl text-center mb-3">
            <span style={{fontFamily:'didot-w02-italic,serif',fontWeight:200}}>Im a product</span>
            </p>
            <p className="text-lg text-center">
            <span className="text-light-orange italic pt-4">$100.00</span>
            </p>
          </div>
        </div>
      </div>
        <button aria-label="Siguiente"  className="block text-black px-3 text-3xl" onClick={() =>moveSlidertoRight()}>
          <i className="fas fa-chevron-right"></i>
        </button>
      </div>
    </section>
  );
};

export default Carousel;
