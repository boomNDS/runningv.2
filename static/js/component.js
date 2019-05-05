Vue.component('Timer', {
    props: ["starttime", "endtime", "trans"],
    data: function() {
        return {
          timer: "",
          wordString: {},
          start: "",
          end: "",
          interval: "",
          days: "",
          minutes: "",
          hours: "",
          seconds: "",
          message: "",
          statusType: "",
          statusText: ""
        };
      },
      created: function() {
        this.wordString = JSON.parse(this.trans);
      },
      mounted() {
        this.start = new Date(this.starttime).getTime();
        this.end = new Date(this.endtime).getTime();
        // Update the count down every 1 second
        this.timerCount(this.start, this.end);
        this.interval = setInterval(() => {
          this.timerCount(this.start, this.end);
        }, 1000);
      },
      methods: {
        timerCount: function(start, end) {
          // Get todays date and time
          var now = new Date().getTime();
    
          // Find the distance between now an the count down date
          var distance = start - now;
          var passTime = end - now;
    
          if (distance < 0 && passTime < 0) {
            this.message = this.wordString.expired;
            this.statusType = "expired";
            this.statusText = this.wordString.status.expired;
            clearInterval(this.interval);
            return;
          } else if (distance < 0 && passTime > 0) {
            this.calcTime(passTime);
            this.message = this.wordString.running;
            this.statusType = "running";
            this.statusText = this.wordString.status.running;
          } else if (distance > 0 && passTime > 0) {
            this.calcTime(distance);
            this.message = this.wordString.upcoming;
            this.statusType = "upcoming";
            this.statusText = this.wordString.status.upcoming;
          }
        },
        calcTime: function(dist) {
          // Time calculations for days, hours, minutes and seconds
          this.days = Math.floor(dist / (1000 * 60 * 60 * 24));
          this.hours = Math.floor(
            (dist % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
          );
          this.minutes = Math.floor((dist % (1000 * 60 * 60)) / (1000 * 60));
          this.seconds = Math.floor((dist % (1000 * 60)) / 1000);
        }
      },
      template: `<div id="timer">
      <div>
        <h3>การแข่งขันกำลังจะเริ่มต้นในอีก</h3>
      </div>
      <!-- <div class="status-tag" :class="statusType">{{ statusText }}</div> -->
      <div v-show="statusType !== 'expired'">
        <div class="day">
          <span class="number">{{ days }}</span>
          <div class="format">{{ wordString.day }}</div>
        </div>
        <div class="hour">
          <span class="number">{{ hours }}</span>
          <div class="format">{{ wordString.hours }}</div>
        </div>
        <div class="min">
          <span class="number">{{ minutes }}</span>
          <div class="format">{{ wordString.minutes }}</div>
        </div>
        <div class="sec">
          <span class="number">{{ seconds }}</span>
          <div class="format">{{ wordString.seconds }}</div>
        </div>
      </div>
      <!-- <div class="message">{{ message }}</div> -->
    </div>`
  })

  Vue.component('rule', {
    props: ['num', 'races'],
      template: `<div class="container is-fluid" id="RunnerRule">
      <div class="columns is-multiline runner">
        <div class="column is-4">
          <h1 class="title">คนที่</h1>
          <p class="num">{{num}}</p>
        </div>
        <div class="column is-8">
          <h1>จะต้องวิ่งช่วง</h1>
          <div class="columns">
            <div class="column is-4 circle" v-for="i in races" :key="i">{{i}}</div>
          </div>
        </div>
      </div>
    </div>`
  })

  Vue.component('cardcategory', {
    props: ['Competition'],
      template: `<div class="CardCategory">
      <div class="container is-fluid">
        <div class="columns is-multiline is-mobile">
          <div class="column is-12">
            <h1>ประเภท{{Competition.title}}</h1>
          </div>
          <div class="column is-5 cardbox" v-for="i in Competition.card" :key="i">
            <h3>{{i.name}}</h3>
            <h2>{{i.age}}</h2>
          </div>
        </div>
      </div>
    </div>`
  })