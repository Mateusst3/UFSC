import { signIn, signOut, useSession } from "next-auth/react";
import { IoIosNotifications } from "react-icons/io";

export default function EnterMenu() {
  const { data: session } = useSession();
  return (
    <>
      <div className="w-auto flex flex-row items-center justify-center gap-3 fixed top-3 right-28">
        <button className="border border-transparent rounded-full p-1 hover:border-blue-700 transition">
          <IoIosNotifications className="text-2xl" />
        </button>
        {!session ? (
          <>
            <button
              className="text-white uppercase border border-transparent hover:border-blue-700 rounded-full px-2 py-1 transition"
              onClick={() => signIn("github")}
            >
              entrar
            </button>
          </>
        ) : (
          <>
            <button className="w-auto flex flex-row items-center justify-center gap-2 bg-blue-700 px-2 py-1 rounded-full" onClick={() => signOut()}>
              <img src={session.user?.image as string} alt="" className="w-6 h-6 rounded-full" />
              <p>{session.user?.name}</p>
            </button>
          </>
        )}
      </div>
    </>
  );
}
