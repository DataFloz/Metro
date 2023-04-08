import { useDisclosure, useInputState } from '@mantine/hooks';
import { Dialog, Group, Button, TextInput, Text } from '@mantine/core';
import { Pipeline } from '@/models/pipeline';
import { Connector } from '@/models/connector';
import axios from 'axios';

interface IProp{
    pipelines: Pipeline[];
    kafkaConnector: Connector;
}

export default function CreateTopics({pipelines, kafkaConnector}: IProp) {
    const [opened, { toggle, close }] = useDisclosure(false);
    
    const initTopics = () => {
        axios.post('/api/create-topics', {pipelines, kafkaConnector}).then(() =>{
            close();
        })
    }

    return (
      <>
        <Group position="center">
          <Button onClick={toggle}>Create all topics</Button>
        </Group>
  
        <Dialog opened={opened} withCloseButton onClose={close} size="lg" radius="md">
          <Text size="sm" mb="xs" weight={500}>
            Create Topics
          </Text>
  
          <Group align="flex-end">
            <Text size="sm" mb="xs">
              This will create all the necessery topics for your metro!
            </Text>
            <Button onClick={initTopics}>Create</Button>
          </Group>
        </Dialog>
      </>
    );
}
