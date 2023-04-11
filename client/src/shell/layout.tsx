import { ActionIcon, AppShell, Col, Footer, Grid, Header, NavLink, useMantineColorScheme } from "@mantine/core";
import { IconBrandGithubFilled, IconMoonStars, IconSun } from "@tabler/icons-react";

type Props = {
    children: string | JSX.Element | JSX.Element[]
}
  
export default function Layout({children}:Props) {
  const { colorScheme, toggleColorScheme } = useMantineColorScheme();
  const dark = colorScheme === 'dark';

  return (
      <>
        <AppShell
            padding="md"
            header={<Header height={60} p="xs" >
                      <Grid grow>
                        <Col span="content">
                          <NavLink component="a" href="/" style={{width:'fit-content'}} label="DataFloz" />
                        </Col>
                      </Grid>
                    </Header>}
            footer={
              <Footer height={60} p="md">
                <Grid>
                    <Grid.Col span={8}>
                        DataFloz - Data stream transformation platform
                    </Grid.Col>
                    <Grid.Col span={1} offset={2}>
                        <ActionIcon component="a" href="https://github.com/DataFloz/Metro">
                            <IconBrandGithubFilled size="1.125rem" />
                        </ActionIcon>
                    </Grid.Col>
                    <Grid.Col span={1}>
                      <ActionIcon
                          variant="outline"
                          color={dark ? 'yellow' : 'blue'}
                          onClick={() => toggleColorScheme()}
                          title="Toggle color scheme"
                        >
                          {dark ? <IconSun size="1.1rem" /> : <IconMoonStars size="1.1rem" />}
                        </ActionIcon>
                    </Grid.Col>
                </Grid>
              </Footer>
            }
            styles={(theme) => ({
              main: { backgroundColor: dark ? theme.colors.dark[8] : theme.colors.gray[0] },
          })}
        >
          {children}
        </AppShell>
      </>
    );
}
