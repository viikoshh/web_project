<template>
  <v-data-table
    :headers="headers"
    :items="transaction"
  ></v-data-table>


</template>

<script>
export default {
  data () {
    return {
      headers: [
        { text: 'Transaction title', value: 'title' },
        { text: 'Amount', value: 'amount' }
      ],
      transaction: [
        {
          title: 'Заправка "Лукойл"',
          amount: '1568.25 руб'
        },
        {
          title: 'Магазин "Zara"',
          amount: '5625.00 руб'
        },
        {
          title: 'Шоколадница',
          amount: '255 руб'
        }
      ]
    }
  }
}
</script>

<style lang="css" scoped></style>
