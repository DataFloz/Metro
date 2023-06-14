import DataProvider from '@/context/context';
import Layout from '@/shell/layout';
import {
    ColorScheme,
    ColorSchemeProvider,
    MantineProvider,
} from '@mantine/core';
import { useState } from 'react';

const Main = ({ Component, pageProps }: any) => {
    const [colorScheme, setColorScheme] = useState<ColorScheme>('light');
    const toggleColorScheme = (value?: ColorScheme) =>
        setColorScheme(value || (colorScheme === 'dark' ? 'light' : 'dark'));

    return (
        <>
            <ColorSchemeProvider
                colorScheme={colorScheme}
                toggleColorScheme={toggleColorScheme}
            >
                <MantineProvider
                    theme={{ colorScheme }}
                    withGlobalStyles
                    withNormalizeCSS
                >
                    <DataProvider>
                        <Layout>
                            <Component {...pageProps} />
                        </Layout>
                    </DataProvider>
                </MantineProvider>
            </ColorSchemeProvider>
        </>
    );
};

export default Main;
