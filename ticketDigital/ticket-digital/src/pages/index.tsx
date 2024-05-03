import DisplayNewEvent from "@/components/displayTicket/DisplayNewEvent";
import DisplayTicketHome from "@/components/displayTicket/DisplayTicketHome";
import SideMenu from "@/components/menu/SideMenu";

export default function Home() {
  return (
    <>
      <main className="flex flex-row">
        <SideMenu />
        <div className="w-full h-full min-h-[80vh] flex flex-col items-start justify-start px-8 py-10 bg-gradient-to-b from-[#F5D342] via-[#587295] to-black gap-12">
          <section className="flex flex-col items-start justify-center gap-3">
            <h4 className="text-white font-bold text-4xl">Olá, Angel</h4>
            <p className="text-white font-bold text-3xl">
              Sugestões para você!
            </p>
          </section>
          <section className="flex flex-wrap justify-between w-full gap-3">
            <DisplayTicketHome image="/images/foto_1.png" name="Tomorrowland" />
            <DisplayTicketHome
              image="/images/foto_4.png"
              name="League of Legends"
            />
            <DisplayTicketHome image="/images/foto_3.png" name="CS:GO Major" />
            <DisplayTicketHome
              image="/images/foto_2.png"
              name="Rolland Garros"
            />
          </section>
          <p className="text-white text-3xl">O que há de novo</p>
          <section className="flex flex-wrap justify-start w-full gap-6">
            <DisplayNewEvent
              image={"/images/image 1.png"}
              name={"Campeonato Carioca"}
              category={"Futebol"}
            />
            <DisplayNewEvent
              image={"/images/image 4.png"}
              name={"Jorge & Mateus"}
              category={"Sertanejo"}
            />
            <DisplayNewEvent
              image={"/images/image 6.png"}
              name={"Paulistão 2024"}
              category={"Futebol"}
            />
            <DisplayNewEvent
              image={"/images/image 3.png"}
              name={"Libertadores"}
              category={"Futebol"}
            />
            <DisplayNewEvent
              image={"/images/image 5.png"}
              name={"CP Atemporal"}
              category={"Forró"}
            />
            <DisplayNewEvent
              image={"/images/image 7.png"}
              name={"Amazonas"}
              category={"Futebol"}
            />
          </section>
        </div>
      </main>
    </>
  );
}
