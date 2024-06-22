import SideMenu from "@/components/menu/SideMenu";
import { FaMagnifyingGlass } from "react-icons/fa6";
import { TiDelete } from "react-icons/ti";

export default function Buscar() {
  return (
    <>
      <main className="flex flex-row">
        <SideMenu />
        <div className="w-full h-full min-h-[80vh] flex flex-col items-start justify-start px-8 py-10 bg-gradient-to-b from-[#F5D342] via-[#587295] to-black gap-12">
          <div className="flex flex-row items-center justify-start gap-1 bg-white rounded-full px-3 py-2">
            <FaMagnifyingGlass className="text-gray-600" />
            <input
              type="text"
              name=""
              placeholder="Shows, jogos ou eventos"
              id=""
              className="rounded-full px-1 text-gray-600"
            />
          </div>
          <div className="w-full flex flex-row items-center justify-start">
            <section className="flex flex-col items-center justify-center p-3 bg-transparent relative">
              <section className="w-full h-full absolute bg-white opacity-25 z-0"></section>
              <button className="absolute top-0 right-0 text-black text-lg">
                <TiDelete />
              </button>
              <img src="/images/image 1.png" alt="" className="z-20" />
              <p className="z-20">Campeonato Carioca</p>
              <p className="z-20">Partida</p>
            </section>
          </div>
          <div className="flex flex-col items-start justify-center gap-4">
            <h3 className="text-4xl">Seus top eventos</h3>
            <section className="flex flex-row items-center justify-start gap-5">
              <div className="h-32 w-80 bg-pink-600 p-3 cursor-pointer">
                <p className="text-2xl font-bol">Festivais</p>
              </div>
              <div className="h-32 w-80 bg-green-200 p-3 cursor-pointer">
                <p className="text-2xl font-bol">Partidas</p>
              </div>
              <div className="h-32 w-80 bg-pink-300 p-3 cursor-pointer">
                <p className="text-2xl font-bol">Shows</p>
              </div>
            </section>
          </div>
        </div>
      </main>
    </>
  );
}
