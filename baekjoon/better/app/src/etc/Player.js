const INIT_MONEY = 10000

export default class Player {

  constructor(name,color){
    this.name = name
    this.color = color
    this.money = INIT_MONEY
    this.tot_bet = 0
    this.cur_bet = 0
    this.is_alive = true
  }

  reset(){
    this.tot_bet = this.cur_bet = 0
    if (this.money !== 0){
      this.is_alive = true
    }
  }
}