#----------------------------------------------------#
# APP -----------------------------
#----------------------------------------------------#

library(plotly)

# Server ---------------------------------------------

server = shinyServer(function(input, output){
  a <- reactive({})
  output$tab_a <- DT::renderDataTable({
    DT::datatable(a())
    })

  plot_a <- reactive({})

  output$plotly_plot_a <- renderPlotly({})
  
  b <- reactive({})
  output$tab_a <- DT::renderDataTable({
    DT::datatable(a())
  })
  
  plot_b <- reactive({})

  output$plotly_plot_b <- renderPlotly({})
  
  })


# Ui -------------------------------------------------

ui = {
  fluidPage(
    mainPanel(
      tabsetPanel(id = 'panel',
                  tabPanel('a',
                           br(),
                           DT::dataTableOutput('tab_a', width = 1500),
                           br(),
                           plotlyOutput('plotly_plot_a')
                  ),
                  tabPanel('b',
                           br(),
                           DT::dataTableOutput('tab_b', width = 1500),
                           br(),
                           plotlyOutput('plotly_plot_b')
                  )
      )
      
      
    )
  )}


# App ------------------------------------------------
shinyApp(ui = ui, server = server)