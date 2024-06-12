import SideMenu from "@/components/menu/SideMenu";
import { useSession } from "next-auth/react";

export default function Tickets() {
  const { data: session } = useSession();
  return (
    <>
      <main className="flex flex-row">
        <SideMenu />
        <div className="w-full h-full min-h-[80vh] flex flex-col items-center justify-start px-8 py-10 bg-gradient-to-b from-[#F5D342] via-[#587295] to-black gap-12">
          {session ? (
            <>
              <img src="/images/qrcode.png" alt="" />
              <div className="w-full h-auto flex flex-col items-center justify-center gap-3">
                <h3 className="text-5xl font-bold">Brasileirão Série A</h3>
                <p className="text-lg">Fluminense x Atlético - MG</p>
                <p className="text-lg">Nome: {session.user?.name}</p>
                <p className="text-lg">Email: {session.user?.email}</p>
              </div>
            </>
          ) : (
            <>
              <h2>Você precisa estar logado para ver seus tickets!</h2>
            </>
          )}
        </div>
      </main>
    </>
  );
}
