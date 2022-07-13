describe('Test Valeur ok', () => {
  it('Pages login', () => {
    cy.visit('http://localhost:8501/')
    cy.get('input').eq(0).clear().type(250)
    cy.get('input').eq(1).clear().type(2)
    cy.get('input').eq(2).clear().type(1)
  })
})

describe('Test Valeur négative taille', () => {
  it('Pages login', () => {
    cy.visit('http://localhost:8501/')
    cy.get('input').eq(0).clear().type(-250)
    cy.get('input').eq(1).clear().type(2)
    cy.get('input').eq(2).clear().type(1)
    cy.get('p').eq(0).contains('mettre taille correcte')
  })
})

describe('Test Valeur négative room', () => {
  it('Pages login', () => {
    cy.visit('http://localhost:8501/')
    cy.get('input').eq(0).clear().type(250)
    cy.get('input').eq(1).clear().type(-2)
    cy.get('input').eq(2).clear().type(1)
    cy.get('p').eq(0).contains('mettre nombre de chambre correct')
  })
})

describe('Test Valeur négative garden', () => {
  it('Pages login', () => {
    cy.visit('http://localhost:8501/')
    cy.get('input').eq(0).clear().type(250)
    cy.get('input').eq(1).clear().type(2)
    cy.get('input').eq(2).clear().type(-1)
    cy.get('p').eq(0).contains('mettre nombre de jardin correct')
  })
})



