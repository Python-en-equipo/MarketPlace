import { IoIosArrowBack } from "react-icons/io";
function ProfileSeller() {
  return (
    <div>
      <header className="h-[50px] flex justify-center items-center">
        <span className="absolute left-4 ">
          <IoIosArrowBack />
        </span>
        <h1 className="text-xl">Profile</h1>
      </header>
      <div className="sm:flex">
        <section className="flex flex-col items-center sm:shrink-0 sm:basis-1/4">
          <div className="rounded-full overflow-hidden flex w-[150px] h-[150px] ">
            <img
              className="w-full object-cover"
              src="https://placeimg.com/640/480/people"
              alt=""
            />
          </div>
          <p className="my-4">Name</p>
          <div className="text-center bg-slate-100 px-4 py-2 sm:self-stretch">
            Datos
          </div>
        </section>
        <section className="mx-2 sm:grow">
          <div className="bg-slate-100 mt-4 px-4 py-2">
            {" "}
            historial de ventas
          </div>
          <div className="bg-slate-100 mt-4 px-4 py-2">
            {" "}
            historial de compras
          </div>
        </section>
      </div>
    </div>
  );
}

export default ProfileSeller;
