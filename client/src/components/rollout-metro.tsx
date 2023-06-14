import { useDisclosure } from '@mantine/hooks';
import { Dialog, Group, Button, Text } from '@mantine/core';
import axios from 'axios';

export default function RolloutMetro() {
    const [opened, { toggle, close }] = useDisclosure(false);

    const SendRollout = () => {
        axios.post('/api/rollout-metro');
        close();
    };

    return (
        <>
            <Group position="center">
                <Button onClick={toggle}>Rollout</Button>
            </Group>

            <Dialog
                opened={opened}
                withCloseButton
                onClose={close}
                size="lg"
                radius="md"
            >
                <Text size="sm" mb="xs" weight={500}>
                    Rollout Metro
                </Text>

                <Group align="flex-end">
                    <Text size="sm" mb="xs">
                        This will your current metro configuration, this action
                        take some time
                    </Text>
                    <Button onClick={SendRollout}>ROLLOUT</Button>
                </Group>
            </Dialog>
        </>
    );
}
