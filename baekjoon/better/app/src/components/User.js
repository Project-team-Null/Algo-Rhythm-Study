import React, {useState,useReducer} from 'react';
import { Button,Avatar,Statistic,Select } from 'antd';
import Player from '../etc/Player';
import userData from '../etc/userData';

const { Option } = Select;

const UserList = userData.map(({name,color}) => new Player(name,color));
const min = (a,b) => a < b ? a : b 
const max = (a,b) => a > b ? a : b 

const User = ({curPool, setCurPool}) => {
  const [_, forceUpdate] = useReducer(num => num + 1, 0);
  function handleChange(){
      forceUpdate();
  }
  const [userIndex, setUserIndex] = useState(0);
  const [color, setColor] = useState(UserList[0].color);
  const [winner_list, setWinner_list] = useState([]);
  const goNext = () => {
    let newIndex = (userIndex + 1) % UserList.length
    if (!UserList[newIndex].is_alive){
      newIndex = (newIndex + 1) % UserList.length
    }
    // 전부다 다이?..일때는?
    setUserIndex(newIndex);
    setColor(UserList[userIndex].color);
  };

  const goPrev = () => {
    let tmp = userIndex !== 0 ? userIndex - 1 : UserList.length - 1
    if (!UserList[tmp].is_alive){
      tmp = tmp !== 0 ? tmp - 1 : UserList.length - 1
    }
    setUserIndex(tmp);
    setColor(UserList[userIndex].color);
  };


  const start_game = () => {
    for (let v of UserList){
      v.money -= curPool.base_bet
    }
    setCurPool({
      max_bet: 0,
      base_bet: 100,
      total_bet: curPool.base_bet * UserList.length
    })

  }

  const die = index => UserList[index].is_alive = false
  const half = index => {
    const player = UserList[index]
    let temp = curPool.total_bet / 2
    temp -= temp % curPool.base_bet
    player.cur_bet = min(temp, player.money)
    handleChange()

  }
  const quarter = p_idx => {
    const player = UserList[p_idx]
    let temp = curPool.total_bet / 4
    temp -= temp % curPool.base_bet
    player.cur_bet = min(temp, player.money)
    handleChange()

  }
  const call = p_idx => {
    const player = UserList[p_idx]
    player.cur_bet = min(curPool.max_bet - player.tot_bet, player.money)
    handleChange()

  }

  const reset_bet = p_idx => {
    UserList[p_idx].cur_bet = 0
    handleChange()
  }
  const add_bet = p_idx => {
    const player = UserList[p_idx]
    let temp = curPool.total_bet / 2
    temp -= temp % curPool.base_bet
    player.cur_bet += min(curPool.base_bet, player.money)
    player.cur_bet = min(player.cur_bet, temp)
    handleChange()
    console.log(player)
  }
  const remove_bet = p_idx => {
    const player = UserList[p_idx]
    player.cur_bet -= min(curPool.base_bet, player.cur_bet)
    handleChange()

  }
  
  const confirm_bet = p_idx => {
    const player = UserList[p_idx]
    player.tot_bet += player.cur_bet
    player.money -= player.cur_bet

    setCurPool({
      max_bet: max(curPool.max_bet, player.tot_bet),
      base_bet: curPool.base_bet,
      total_bet:curPool.total_bet + player.cur_bet,
      })
    player.cur_bet = 0
    console.log(curPool)
    handleChange()
  }
  const turn_change = () =>{
    setCurPool({
      ...curPool,
      max_bet:0
    })
    for (let v of UserList){
      v.tot_bet = 0
      v.cur_bet = 0
    }
  }
  const end_game = winner_list => {
    for (let idx in winner_list){
      const player = UserList[idx]
      player.money += curPool.total_bet / winner_list.length
    }
    setCurPool({
      ...curPool,
      max_bet:0,
      total_bet:0
    })
    for (let v in UserList){
      UserList[v].reset()
    }
    handleChange()
    
  }
  return (
  <div className="user">
    <div className='user-info'>
      <Button
          type='primary'
          size="large"
          shape='round'
          style={{
            margin: '0 16px',
            verticalAlign: 'middle',
          }}
          onClick={goPrev}
        >
          Prev
      </Button>
      <Avatar
        style={{
          backgroundColor: color,
          verticalAlign: 'middle',
        }}
        size={72}
      >
        {UserList[userIndex].name}
      </Avatar>
      <Button
        type='primary'
        size="large"
        shape='round'
        style={{

          margin: '0 16px',
          verticalAlign: 'middle',
        }}
        onClick={goNext}
      >
        Next
      </Button>
    </div>

    <div className='button-list'>
      {[["start_game",start_game],["die",()=>die(userIndex)],["half",()=>half(userIndex)],["quarter",()=>quarter(userIndex)],
      ["call",()=>call(userIndex)], ["reset_bet",()=>reset_bet(userIndex)],["add_bet",()=>add_bet(userIndex)],
      ["remove_bet",()=>remove_bet(userIndex)],["confirm_bet",()=>confirm_bet(userIndex)],["turn_change",turn_change],["end_game",()=>end_game(winner_list)]]
        .map(v=>getBettingButton(...v))}
    </div>
    <Select defaultValue="승자선택" style={{ width: 120 }} onChange={(v)=>{
      setWinner_list([v])}}>
      <Option value="disabled" disabled>
        Disabled
      </Option>
      {UserList.map((v,i)=><Option value={i}>{v.name}</Option>)}
    </Select>
    <div className='user-status'>
      <Statistic title="내돈" value={UserList[userIndex].money} />
      <Statistic title="낼돈" value={UserList[userIndex].cur_bet} />      
    </div>
  
  </div>)
}

export default User;

// 하프 쿼터 리셋 더하기 빼기 콜

const getBettingButton = (name,fn) => {
  return (      <Button
    type='primary'
    size="large"
    shape='round'
    style={{
      margin: '0 16px',
      width: "200px",
      verticalAlign: 'middle',
    }}
    onClick={fn}
  >
    {name}
</Button>  )
}