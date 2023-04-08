import { PipelineList } from "@/models/pipeline-list";
import React, { FC, ReactNode, useContext } from "react";
export type DataContextType = {
  config: PipelineList,
  updateConfig: (config: PipelineList) => void;

}

type Props = {
  children: ReactNode;
};

export const DataContext = React.createContext<DataContextType | null>(null);

export const useDataContext = () => {
  return useContext(DataContext)
}
const DataProvider = ({ children }: Props): JSX.Element => {
  const [config, setConfig] = React.useState<PipelineList>({
    'name': '',
    pipelines: [],
    connectors: [{
      name: '',
      brokers: '',
      group_id: ''
    }]
  });
  
  const updateConfig = (config: PipelineList) => {
    setConfig(config);
  };

  return (
    <DataContext.Provider value={{ config, updateConfig }}>
      {children}
    </DataContext.Provider>
  );
};

export default DataProvider;
