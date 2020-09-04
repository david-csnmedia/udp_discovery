# UDP Discovery

This simple module can be configured as something as simple as a cron job that broadcasts itself every minute, to something more robust.

## Broadcasting

<pre>
python -m udp_discovery broadcast <em>27000 service_name</em>
</pre>

## Receiving the broadcast

<pre>
python -m udp_discovery discover <em>27000 service_name</em>
</pre>

---

## Serve Broadcasts

<pre>
python -m udp_discovery serve <em>27000 service_name</em>
</pre>

## Quick Discovery

<pre>
python -m udp_discovery discover_fast <em>27000 service_name</em>
</pre>

