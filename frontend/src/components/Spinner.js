
const Spinner = () => {
  return (
    <section className="absolute w-screen h-screen z-20 bg-white top-0 left-0 grid place-content-center">
      <div className="relative w-16 h-16 border-8 border-t-red-500 rounded-full animate-spin"></div>
    </section>
  )
}

export default Spinner