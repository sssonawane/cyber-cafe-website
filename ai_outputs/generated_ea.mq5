//+------------------------------------------------------------------+
//|                                                   generated_ea.mq5 |
//|                   Demo EA – Session Based (MT5)                  |
//+------------------------------------------------------------------+
#property strict

#include <Trade/Trade.mqh>
CTrade trade;

// ================= SESSION INPUTS =================
input bool UseLondonSession  = true;
input int  LondonStartHour   = 8;
input int  LondonEndHour     = 17;

input bool UseNewYorkSession = true;
input int  NYStartHour       = 13;
input int  NYEndHour         = 22;
// =================================================

// ================= TRADE INPUTS =================
input double LotSize          = 0.01;
input int    StopLossPoints   = 300;
input int    TakeProfitPoints = 600;
// =================================================


//+------------------------------------------------------------------+
//| Check Trading Session                                            |
//+------------------------------------------------------------------+
bool IsTradingSession()
{
   datetime now = TimeCurrent();
   int hour = TimeHour(now);

   bool inLondon = false;
   bool inNY     = false;

   if(UseLondonSession)
      inLondon = (hour >= LondonStartHour && hour <= LondonEndHour);

   if(UseNewYorkSession)
      inNY = (hour >= NYStartHour && hour <= NYEndHour);

   return (inLondon || inNY);
}

//+------------------------------------------------------------------+
//| Expert initialization                                           |
//+------------------------------------------------------------------+
int OnInit()
{
   Print("generated_ea initialized successfully");
   return INIT_SUCCEEDED;
}

//+------------------------------------------------------------------+
//| Expert deinitialization                                         |
//+------------------------------------------------------------------+
void OnDeinit(const int reason)
{
   Print("generated_ea removed");
}

//+------------------------------------------------------------------+
//| Expert tick function                                            |
//+------------------------------------------------------------------+
void OnTick()
{
   if(!IsTradingSession())
      return;

   if(PositionSelect(_Symbol))
      return;

   double ask = SymbolInfoDouble(_Symbol, SYMBOL_ASK);
   if(ask <= 0)
      return;

   double sl = ask - StopLossPoints * _Point;
   double tp = ask + TakeProfitPoints * _Point;

   trade.Buy(LotSize, _Symbol, ask, sl, tp, "Session Buy");
}
//+------------------------------------------------------------------+
