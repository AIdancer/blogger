### 一个Go编写的简单的prometheus自定义exporter
```go
package main

import (
	"flag"
	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
	"log"
	"net/http"
	"time"
)

var addr = flag.String("listen-address", ":8088", "The address to listen on for http requests")

var (
	//Gauge 仪表盘类型
	opsQueued = prometheus.NewGauge(prometheus.GaugeOpts{
		Namespace: "our_company",
		Subsystem: "blob_storage",
		Name:      "ops_queued",
		Help:      "Number of blob storage operations waiting to be processed",
	})

	jobsInQueue = prometheus.NewGaugeVec(prometheus.GaugeOpts{
		Name: "job_in_queue",
		Help: "Current number of jobs in the queue",
	}, []string{"job_type"})

	//Count 计数器类型
	taskCounter = prometheus.NewCounter(prometheus.CounterOpts{
		Subsystem: "worker_pool",
		Name:      "completed_tasks_total",
		Help:      "Total number of tasks completed.",
	})

	//Summary 类型，需要提供分位点
	temps = prometheus.NewSummary(prometheus.SummaryOpts{
		Name:       "pond_temperature_celsius",
		Help:       "The temperature of the frog pond.",
		Objectives: map[float64]float64{0.5: 0.05, 0.9: 0.01, 0.99: 0.001},
	})

	//Histogram 类型，需要提供 Bucket大小
	tempsHistogram = prometheus.NewHistogram(prometheus.HistogramOpts{
		Name:        "pond_temperature_histogram_celsius",
		Help:        "The temperature of the frog pond.",
		ConstLabels: nil,
		Buckets:     prometheus.LinearBuckets(20, 5, 5), // 5 个 buckets, 跨度为 5 摄氏度.
		//Buckets:     []float64{20, 25, 30, 35, 40}, //等价于这个
	})
)

func init() {
	prometheus.MustRegister(opsQueued, jobsInQueue, taskCounter, temps, tempsHistogram)
}

func main() {
	flag.Parse()
	jobsInQueue.WithLabelValues("testjob").Add(3)
	go func() {
		for true {
			opsQueued.Add(4)
			time.Sleep(time.Second)
			taskCounter.Inc()
		}
	}()
	http.Handle("/metrics", promhttp.Handler())
	log.Fatal(http.ListenAndServe(*addr, nil))
}

```
其中go.mod依赖如下  
```
module my-exporter

go 1.19

require github.com/prometheus/client_golang v1.1.0

require (
	github.com/beorn7/perks v1.0.1 // indirect
	github.com/matttproud/golang_protobuf_extensions v1.0.1 // indirect
	github.com/prometheus/client_model v0.3.0 // indirect
	github.com/prometheus/common v0.6.0 // indirect
	github.com/prometheus/procfs v0.0.3 // indirect
	golang.org/x/sys v0.0.0-20190916202348-b4ddaad3f8a3 // indirect
)
```
