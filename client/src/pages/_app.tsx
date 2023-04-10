import DataProvider from "@/context/context";
import Layout from "@/shell/layout";
import { AppShell, Footer, Header } from "@mantine/core";

const Main = ({ Component, pageProps }: any) => {
  return (
    <>
      <DataProvider>
        <Layout>
          <Component {...pageProps} />
        </Layout>
      </DataProvider>
    </>
  );
}

export default Main