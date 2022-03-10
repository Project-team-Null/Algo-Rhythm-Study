
import React from 'react';
import { Statistic, Row, Col } from 'antd';


const Pool = ({curPool}) => (
      <div className="pool">
        <Row gutter={16}>
          <Col span={12}>
            <Statistic title="현재 총액" value={curPool.total_bet} />
          </Col>
          <Col span={12}>
            <Statistic title="판돈 / 점당" value={curPool.base_bet}/>
          </Col>
        </Row>
      </div>
);

export default Pool;


