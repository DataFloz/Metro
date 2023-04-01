import { useDisclosure, useInputState } from '@mantine/hooks';
import { Dialog, Group, Button, TextInput, Text } from '@mantine/core';
import { Pipeline } from '@/models/pipeline';
import { Connector } from '@/models/connector';
import axios from 'axios';

interface ProduceTest{
    pipeline: Pipeline;
    kafkaConnector: Connector;
}

export default function ProduceTest({pipeline, kafkaConnector}:ProduceTest) {
    const [opened, { toggle, close }] = useDisclosure(false);
    const [messageValue, setMessageValue] = useInputState(undefined);
    
    const sendTestMessage = () => {
        axios.post('/api/test', {pipeline, kafkaConnector, message: messageValue}).then(() =>{
            close();
        })
    }

    return (
      <>
        <Group position="center">
          <Button onClick={toggle}>Produce test message</Button>
        </Group>
  
        <Dialog opened={opened} withCloseButton onClose={close} size="lg" radius="md">
          <Text size="sm" mb="xs" weight={500}>
            Producing Test message to the selected pipeline
          </Text>
  
          <Group align="flex-end">
            <TextInput value={messageValue} onChange={setMessageValue}  placeholder="message value" sx={{ flex: 1 }} />
            <Button onClick={sendTestMessage}>Send</Button>
          </Group>
        </Dialog>
      </>
    );
}
