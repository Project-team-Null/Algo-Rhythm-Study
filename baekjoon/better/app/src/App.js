import React, {useState} from 'react';
import { Layout } from 'antd';

import Pool from './components/Pool';
import User from './components/User';
import './App.css';


const { Header, Footer, Content } = Layout;

const initPool = {
  max_bet: 0,
  base_bet: 100,
  total_bet: 0,
}

const App = () => {
  const [curPool, setCurPool] = useState(initPool);
  return (
    <><Layout>
      <Header>Better</Header>
      <Content style={{ padding: '50px' }}>
        <Pool curPool = {curPool}></Pool>
        <User setCurPool = {setCurPool} curPool = {curPool} ></User>
      </Content>
      <Footer className="footer">Footer</Footer>
    </Layout></>
  );
}

export default App;


