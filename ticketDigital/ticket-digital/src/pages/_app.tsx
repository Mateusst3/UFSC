import Footer from "@/components/Footer/Footer";
import SideMenu from "@/components/menu/SideMenu";
import EnterMenu from "@/components/enterMenu/EnterMenu";
import "@/styles/globals.css";
import type { AppProps } from "next/app";
import { SessionProvider } from "next-auth/react";

export default function App({
  Component,
  pageProps: { session, ...pageProps },
}: AppProps) {
  return (
    <>
      <SessionProvider>
        <EnterMenu />
        <Component {...pageProps} />
        <Footer />
      </SessionProvider>
    </>
  );
}
