import DataProvider from "@/context/context";

const Main = ({ Component, pageProps }: any) => {
  return (
    <>
      <DataProvider>
          <Component {...pageProps} />
      </DataProvider>
    </>
  );
}

export default Main